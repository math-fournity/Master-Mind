"""SQLite 数据库: 命主档案、星盘、矫正、大限。
单文件 .db, 零部署, AI 用 sqlite3 即可读写。
"""
import sqlite3, json, os
from datetime import datetime

DEFAULT_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "qizheng.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS subject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER,
    birth_ut TEXT,           -- ISO: 1990-05-15T03:30
    birth_lon REAL,
    birth_lat REAL,
    birth_zone TEXT,
    time_uncertainty TEXT,   -- 时间窗口描述，如 "03:00-05:00 不确定"
    note TEXT,
    created TEXT
);

CREATE TABLE IF NOT EXISTS life_event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    year INTEGER,
    event_type TEXT,         -- 'marriage'/'career'/'health'/'move'/'birth'/'death'/'other'
    description TEXT,
    created TEXT,
    FOREIGN KEY(subject_id) REFERENCES subject(id)
);

CREATE TABLE IF NOT EXISTS chart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    jd REAL NOT NULL,
    params_json TEXT,        -- 排盘参数 (ayanamsa, house_system 等)
    bodies_json TEXT,        -- 七政四余天体位置
    houses_json TEXT,        -- 宫头 + ASC/MC
    life_sign REAL,
    child_limit_years INTEGER,
    created TEXT,
    FOREIGN KEY(subject_id) REFERENCES subject(id)
);

CREATE TABLE IF NOT EXISTS rectification (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    original_ut TEXT,
    corrected_ut TEXT,
    method TEXT,             -- 'sun_transit' / 'planet_transit' / 'cs41_optimize'
    target_json TEXT,
    result_json TEXT,
    delta_hours REAL,
    created TEXT,
    FOREIGN KEY(subject_id) REFERENCES subject(id)
);

CREATE TABLE IF NOT EXISTS daxian (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    chart_id INTEGER,
    age INTEGER,
    daxian_current_json TEXT,
    daxian_all_json TEXT,
    small_limit REAL,
    fly_limit REAL,
    created TEXT,
    FOREIGN KEY(subject_id) REFERENCES subject(id),
    FOREIGN KEY(chart_id) REFERENCES chart(id)
);
"""

def get_db(path=None):
    path = path or DEFAULT_DB
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn

def add_subject(conn, name, sex=None, birth_ut=None, birth_lon=None, birth_lat=None, birth_zone=None, time_uncertainty=None, note=None):
    now = datetime.utcnow().isoformat()
    cur = conn.execute(
        "INSERT INTO subject(name,sex,birth_ut,birth_lon,birth_lat,birth_zone,time_uncertainty,note,created) VALUES(?,?,?,?,?,?,?,?,?)",
        (name, sex, birth_ut, birth_lon, birth_lat, birth_zone, time_uncertainty, note, now))
    conn.commit()
    return cur.lastrowid

def update_subject(conn, sid, **fields):
    """更新命主字段，支持 name/sex/birth_ut/birth_lon/birth_lat/birth_zone/time_uncertainty/note"""
    allowed = {"name","sex","birth_ut","birth_lon","birth_lat","birth_zone","time_uncertainty","note"}
    updates = {k: v for k, v in fields.items() if k in allowed}
    if not updates:
        return False
    set_clause = ", ".join(f"{k}=?" for k in updates)
    values = list(updates.values()) + [sid]
    cur = conn.execute(f"UPDATE subject SET {set_clause} WHERE id=?", values)
    conn.commit()
    return cur.rowcount > 0

def delete_subject(conn, sid):
    """级联删除命主及其所有关联记录"""
    for table in ("life_event", "chart", "rectification", "daxian"):
        conn.execute(f"DELETE FROM {table} WHERE subject_id=?", (sid,))
    cur = conn.execute("DELETE FROM subject WHERE id=?", (sid,))
    conn.commit()
    return cur.rowcount > 0

def add_life_event(conn, sid, year, event_type, description):
    now = datetime.utcnow().isoformat()
    cur = conn.execute(
        "INSERT INTO life_event(subject_id,year,event_type,description,created) VALUES(?,?,?,?,?)",
        (sid, year, event_type, description, now))
    conn.commit()
    return cur.lastrowid

def list_life_events(conn, sid):
    return [dict(r) for r in conn.execute(
        "SELECT * FROM life_event WHERE subject_id=? ORDER BY year", (sid,))]

def get_rectification_history(conn, sid):
    return [dict(r) for r in conn.execute(
        "SELECT * FROM rectification WHERE subject_id=? ORDER BY id", (sid,))]

def list_charts_for_subject(conn, sid):
    return [dict(r) for r in conn.execute(
        "SELECT * FROM chart WHERE subject_id=? ORDER BY id", (sid,))]

def list_daxian_for_subject(conn, sid):
    return [dict(r) for r in conn.execute(
        "SELECT * FROM daxian WHERE subject_id=? ORDER BY age", (sid,))]

def add_chart(conn, subject_id, jd, params, bodies, houses, life_sign, child_limit_years):
    now = datetime.utcnow().isoformat()
    cur = conn.execute(
        "INSERT INTO chart(subject_id,jd,params_json,bodies_json,houses_json,life_sign,child_limit_years,created) VALUES(?,?,?,?,?,?,?,?)",
        (subject_id, jd, json.dumps(params,ensure_ascii=False), json.dumps(bodies,ensure_ascii=False),
         json.dumps(houses,ensure_ascii=False), life_sign, child_limit_years, now))
    conn.commit()
    return cur.lastrowid

def add_rectification(conn, subject_id, original_ut, corrected_ut, method, target, result, delta_hours):
    now = datetime.utcnow().isoformat()
    cur = conn.execute(
        "INSERT INTO rectification(subject_id,original_ut,corrected_ut,method,target_json,result_json,delta_hours,created) VALUES(?,?,?,?,?,?,?,?)",
        (subject_id, original_ut, corrected_ut, method,
         json.dumps(target,ensure_ascii=False), json.dumps(result,ensure_ascii=False), delta_hours, now))
    conn.commit()
    return cur.lastrowid

def add_daxian(conn, subject_id, age, daxian_current, daxian_all, small_limit, fly_limit, chart_id=None):
    now = datetime.utcnow().isoformat()
    cur = conn.execute(
        "INSERT INTO daxian(subject_id,chart_id,age,daxian_current_json,daxian_all_json,small_limit,fly_limit,created) VALUES(?,?,?,?,?,?,?,?)",
        (subject_id, chart_id, age,
         json.dumps(daxian_current,ensure_ascii=False), json.dumps(daxian_all,ensure_ascii=False),
         small_limit, fly_limit, now))
    conn.commit()
    return cur.lastrowid

def list_subjects(conn):
    return [dict(r) for r in conn.execute("SELECT * FROM subject ORDER BY id")]

def get_subject(conn, sid):
    r = conn.execute("SELECT * FROM subject WHERE id=?", (sid,)).fetchone()
    return dict(r) if r else None
