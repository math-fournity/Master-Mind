#!/usr/bin/env python3
"""解码Devin CLI的GetChatMessage Connect streaming protobuf响应，提取流式thinking数据。

用法：
  python3 decode_connect_proto.py <file.bin>          # 解码单个文件
  python3 decode_connect_proto.py <dir>               # 解码目录下所有.bin文件
  python3 decode_connect_proto.py <file.bin> --stream  # 只输出thinking流（按时间顺序）

Connect streaming protocol:
  每个envelope: 1 byte flags + 4 bytes length (big-endian) + protobuf message
  flags bit 1 (0x02) = end-of-stream
  
Protobuf字段（通过strings分析devin二进制+decode_raw推断）：
  field 1: message_id (string)
  field 2: timestamp (message: field 1 = seconds, field 2 = nanos)
  field 5: stop_reason (varint)
  field 6: tool_call chunk (message: field 1 = tool_call_id, field 2 = tool_name, field 3 = arguments_chunk)
  field 7: metadata (message: field 6 = ?, field 8 = headers, field 9 = model)
  field 9: content/thinking chunk (string) — 这是流式thinking/content文本
  field 12: sequence number (64bit)
  field 17: session_id (string)
  field 28: statistics (message)
"""
import struct
import os
import sys
import json
from datetime import datetime

def decode_varint(data, pos):
    result = 0
    shift = 0
    while pos < len(data):
        byte = data[pos]
        result |= (byte & 0x7F) << shift
        shift += 7
        pos += 1
        if not (byte & 0x80):
            break
    return result, pos

def decode_protobuf(data):
    pos = 0
    results = []
    while pos < len(data):
        try:
            tag, pos = decode_varint(data, pos)
            field_num = tag >> 3
            wire_type = tag & 0x07
            
            if wire_type == 0:
                value, pos = decode_varint(data, pos)
                results.append((field_num, "varint", value))
            elif wire_type == 1:
                value = struct.unpack('<Q', data[pos:pos+8])[0]
                pos += 8
                results.append((field_num, "64bit", value))
            elif wire_type == 2:
                length, pos = decode_varint(data, pos)
                if pos + length > len(data):
                    break
                value = data[pos:pos+length]
                pos += length
                try:
                    text = value.decode('utf-8')
                    if all(c.isprintable() or c in '\n\r\t' for c in text[:50]):
                        results.append((field_num, "string", text))
                    else:
                        nested = decode_protobuf(value)
                        results.append((field_num, "message", nested))
                except:
                    try:
                        nested = decode_protobuf(value)
                        results.append((field_num, "message", nested))
                    except:
                        results.append((field_num, "bytes", value.hex()[:100]))
            elif wire_type == 5:
                value = struct.unpack('<I', data[pos:pos+4])[0]
                pos += 4
                results.append((field_num, "32bit", value))
            else:
                break
        except:
            break
    return results

def parse_connect_stream(data):
    messages = []
    pos = 0
    while pos + 5 <= len(data):
        flags = data[pos]
        length = struct.unpack('>I', data[pos+1:pos+5])[0]
        pos += 5
        if pos + length > len(data):
            msg_data = data[pos:]
            messages.append((flags, msg_data))
            break
        msg_data = data[pos:pos+length]
        pos += length
        messages.append((flags, msg_data))
    return messages

def extract_streaming_data(filepath):
    """从GetChatMessage响应中提取流式thinking/content/tool_call数据
    
    流式协议特点：
    - field 9 (string): content/thinking chunk，逐token流式
    - field 6 (message): tool_call chunk
      - sub-field 1: tool_call_id（仅首个chunk出现）
      - sub-field 2: tool_name（仅首个chunk出现）
      - sub-field 3: arguments chunk（逐token流式，后续chunk只有sub-field 3）
    - 后续tool_call chunks没有tool_call_id，需要"当前活跃tool_call"状态跟踪
    """
    with open(filepath, "rb") as f:
        data = f.read()
    
    messages = parse_connect_stream(data)
    
    content_chunks = []
    tool_call_chunks = {}  # tool_call_id -> {"name": str, "args": str}
    tool_call_order = []  # 保持顺序
    current_tc_id = None  # 当前活跃的tool_call（用于无id的后续chunks）
    stats = None
    
    for flags, msg_data in messages:
        decoded = decode_protobuf(msg_data)
        
        for field_num, type_name, value in decoded:
            if field_num == 9 and type_name == "string":
                content_chunks.append(value)
            elif field_num == 6 and type_name == "message":
                # 解析tool_call chunk
                tc_id = None
                tc_name = ""
                tc_args = ""
                for fn, ft, fv in value:
                    if fn == 1 and ft == "string":
                        tc_id = fv
                    elif fn == 2 and ft == "string":
                        tc_name = fv
                    elif fn == 3 and ft == "string":
                        tc_args = fv
                
                if tc_id:
                    # 新tool_call开始
                    current_tc_id = tc_id
                    if tc_id not in tool_call_chunks:
                        tool_call_chunks[tc_id] = {"name": "", "args": ""}
                        tool_call_order.append(tc_id)
                    tool_call_chunks[tc_id]["name"] += tc_name
                    tool_call_chunks[tc_id]["args"] += tc_args
                elif current_tc_id:
                    # 当前tool_call的后续chunks（只有args）
                    tool_call_chunks[current_tc_id]["args"] += tc_args
            elif field_num == 28 and type_name == "message":
                stats = value
    
    # 按顺序构建tool_calls
    ordered_tool_calls = {tc_id: tool_call_chunks[tc_id] for tc_id in tool_call_order}
    
    return {
        "content_thinking": "".join(content_chunks),
        "content_chunks_count": len(content_chunks),
        "tool_calls": ordered_tool_calls,
        "stats": stats,
        "total_messages": len(messages),
    }

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    path = sys.argv[1]
    stream_mode = "--stream" in sys.argv
    
    files = []
    if os.path.isdir(path):
        files = sorted([os.path.join(path, f) for f in os.listdir(path) if f.endswith(".bin") and "_req" not in f])
    else:
        files = [path]
    
    for fpath in files:
        result = extract_streaming_data(fpath)
        
        if stream_mode:
            print(f"\n=== {os.path.basename(fpath)} ===")
            print(f"Messages: {result['total_messages']}")
            print(f"Content/Thinking ({result['content_chunks_count']} chunks):")
            print(result['content_thinking'][:2000])
            if result['tool_calls']:
                print(f"\nTool calls ({len(result['tool_calls'])}):")
                for tc_id, tc in result['tool_calls'].items():
                    print(f"  {tc['name']}({tc['args'][:200]})")
        else:
            print(f"\n{'='*60}")
            print(f"File: {fpath}")
            print(f"{'='*60}")
            print(json.dumps(result, indent=2, ensure_ascii=False, default=str))

if __name__ == "__main__":
    main()
