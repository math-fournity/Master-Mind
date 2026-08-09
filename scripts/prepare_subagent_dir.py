#!/usr/bin/env python3
"""
为subagent准备工作目录和checklist。
用法: python3 prepare_subagent_dir.py <problem_id> <file_path> <source>
输出: subagent工作目录路径
"""
import sys
import os
from arango import ArangoClient

def prepare(problem_id, file_path, source):
    client = ArangoClient(hosts='http://localhost:8529')
    db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
    
    # 查找progress记录的_key
    docs = list(db.aql.execute(
        f'FOR p IN problem_extraction_progress FILTER p.problem_id == "{problem_id}" RETURN p._key'
    ))
    progress_key = docs[0] if docs else 'UNKNOWN'
    
    # 创建工作目录
    work_dir = f'subagents-dirs/{problem_id}'
    os.makedirs(work_dir, exist_ok=True)
    
    # 读取模板并填充
    template_path = 'subagents-dirs/checklist-template.md'
    with open(template_path, 'r') as f:
        template = f.read()
    
    checklist = template.replace('{{PROBLEM_ID}}', problem_id) \
                       .replace('{{FILE_PATH}}', file_path) \
                       .replace('{{SOURCE}}', source) \
                       .replace('{{PROGRESS_KEY}}', progress_key)
    
    checklist_path = os.path.join(work_dir, 'checklist.md')
    with open(checklist_path, 'w') as f:
        f.write(checklist)
    
    print(work_dir)
    return work_dir

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'用法: {sys.argv[0]} <problem_id> <file_path> <source>')
        sys.exit(1)
    prepare(sys.argv[1], sys.argv[2], sys.argv[3])
