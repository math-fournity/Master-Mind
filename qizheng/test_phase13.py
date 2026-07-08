#!/usr/bin/env python3
"""Phase 13 验证脚本：创建命主→加事件→更新→查关联→删除"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db import get_db, add_subject, update_subject, delete_subject, add_life_event, list_life_events, get_rectification_history, list_charts_for_subject, list_daxian_for_subject, add_chart, add_rectification, add_daxian

def run():
    # 用临时数据库
    db_path = "/tmp/qizheng_phase13_test.db"
    if os.path.exists(db_path):
        os.unlink(db_path)
    conn = get_db(db_path)

    # 1. 创建命主
    sid = add_subject(conn, "测试用户", sex=1, birth_ut="1990-05-15T03:30",
                      birth_lon=116.4, birth_lat=39.9, birth_zone="Asia/Shanghai",
                      time_uncertainty="03:00-05:00 不确定")
    assert sid > 0, "创建命主失败"
    print(f"✓ 创建命主: id={sid}")

    # 2. 更新命主
    ok = update_subject(conn, sid, name="测试用户2", time_uncertainty="03:30 确定时间")
    assert ok, "更新命主失败"
    print(f"✓ 更新命主: name=测试用户2")

    # 3. 添加生命事件
    eid1 = add_life_event(conn, sid, 2015, "marriage", "结婚")
    eid2 = add_life_event(conn, sid, 2018, "career", "升职")
    assert eid1 > 0 and eid2 > 0, "添加事件失败"
    print(f"✓ 添加事件: {eid1}(结婚), {eid2}(升职)")

    # 4. 查询事件
    events = list_life_events(conn, sid)
    assert len(events) == 2, f"事件数应为2，实际{len(events)}"
    print(f"✓ 查询事件: {len(events)}条")

    # 5. 添加星盘
    cid = add_chart(conn, sid, 2458000.5, {"ayanamsa": "lahiri"},
                    {"sun": 50.0}, {"asc": 100.0}, 30.0, 10)
    assert cid > 0, "添加星盘失败"
    print(f"✓ 添加星盘: id={cid}")

    # 6. 添加矫正记录
    rid = add_rectification(conn, sid, "1990-05-15T03:30", "1990-05-15T04:00",
                            "sun_transit", {"target": "sun"}, {"result": "ok"}, 0.5)
    assert rid > 0, "添加矫正失败"
    print(f"✓ 添加矫正: id={rid}")

    # 7. 添加大限
    did = add_daxian(conn, sid, 30, {"limit": 5}, {"all": [1,2,3]}, 5.0, 3.0, chart_id=cid)
    assert did > 0, "添加大限失败"
    print(f"✓ 添加大限: id={did}")

    # 8. 查询关联数据
    charts = list_charts_for_subject(conn, sid)
    assert len(charts) == 1, f"星盘数应为1，实际{len(charts)}"
    print(f"✓ 查询星盘: {len(charts)}条")

    rect_history = get_rectification_history(conn, sid)
    assert len(rect_history) == 1, f"矫正记录应为1，实际{len(rect_history)}"
    print(f"✓ 查询矫正历史: {len(rect_history)}条")

    daxian_list = list_daxian_for_subject(conn, sid)
    assert len(daxian_list) == 1, f"大限记录应为1，实际{len(daxian_list)}"
    print(f"✓ 查询大限: {len(daxian_list)}条")

    # 9. 删除命主（级联删除）
    ok = delete_subject(conn, sid)
    assert ok, "删除命主失败"
    print(f"✓ 删除命主: {ok}")

    # 验证级联删除
    events_after = list_life_events(conn, sid)
    charts_after = list_charts_for_subject(conn, sid)
    assert len(events_after) == 0 and len(charts_after) == 0, "级联删除失败"
    print(f"✓ 级联删除验证: 事件={len(events_after)}, 星盘={len(charts_after)}")

    conn.close()
    os.unlink(db_path)
    print("\n=== Phase 13 验证全部通过 ===")

if __name__ == "__main__":
    run()
