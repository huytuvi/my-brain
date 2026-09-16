#!/usr/bin/env python3
"""
Simon Center Second Brain - Safe Data Synchronization Script
Đồng bộ an toàn 2 chiều giữa JSON Backup (Web) và SQLite brain.db.
Đảm bảo 100% không bao giờ ghi đè hoặc xóa mất tri thức đã thu thập khi cập nhật code phần mềm.
"""

import os
import sys
import json
import sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'brain.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def export_db_to_json(output_path=None):
    """Xuất toàn bộ dữ liệu từ SQLite brain.db ra file JSON để nạp vào Web."""
    if not os.path.exists(DB_PATH):
        print(f"❌ Không tìm thấy database tại {DB_PATH}")
        return None

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM voice_evaluations ORDER BY id ASC")
    eval_rows = [dict(r) for r in cur.fetchall()]

    cur.execute("SELECT * FROM brand_voice ORDER BY id ASC")
    voice_rows = [dict(r) for r in cur.fetchall()]

    cur.execute("SELECT * FROM knowledge ORDER BY id ASC")
    know_rows = [dict(r) for r in cur.fetchall()]

    conn.close()

    export_data = {
        "appName": "Simon Center Second Brain",
        "version": "2.5",
        "exportedAt": datetime.now().isoformat(),
        "source": "SQLite brain.db",
        "evaluations": eval_rows,
        "brand_voice": voice_rows,
        "knowledge": know_rows
    }

    if not output_path:
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(BASE_DIR, f"brain_backup_from_db_{date_str}.json")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Đã xuất tri thức từ brain.db thành công ra: {output_path}")
    print(f"   - {len(eval_rows)} bản ghi đánh giá SOP & bài học")
    print(f"   - {len(voice_rows)} bản ghi cấu hình Brand Voice")
    return output_path

def import_json_to_db(json_path):
    """Hợp nhất (Merge an toàn) dữ liệu từ file JSON vào SQLite brain.db mà không ghi đè."""
    if not os.path.exists(json_path):
        print(f"❌ Không tìm thấy file JSON tại {json_path}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS voice_evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day_number INTEGER NOT NULL,
            voice_key TEXT NOT NULL,
            voice_name TEXT NOT NULL,
            channel TEXT,
            topic TEXT NOT NULL,
            score REAL NOT NULL,
            audience_feedback TEXT,
            voice_rules_added TEXT,
            review_notes TEXT,
            blacklist TEXT,
            case_study TEXT,
            gold_sample TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    eval_list = data.get('evaluations', [])
    inserted_evals = 0

    for item in eval_list:
        day = item.get('day') or item.get('day_number') or 1
        v_key = item.get('voiceKey') or item.get('voice_key') or 'voice1'
        v_name = item.get('voiceName') or item.get('voice_name') or 'Giọng 1'
        channel = item.get('channel') or ''
        topic = item.get('topic') or 'Chăm sóc cột sống'
        score = float(item.get('score', 9.0))
        feedback = item.get('feedback') or item.get('audience_feedback') or ''
        rules = item.get('rules') or item.get('voice_rules_added') or ''
        blacklist = item.get('blacklist') or ''
        case_study = item.get('caseStudy') or item.get('case_study') or ''
        gold_sample = item.get('goldSample') or item.get('gold_sample') or ''
        notes = item.get('review_notes') or ''

        # Check duplicate before insert (Idempotent merge)
        cur.execute('''
            SELECT id FROM voice_evaluations 
            WHERE day_number = ? AND voice_key = ? AND score = ? AND (blacklist = ? OR (blacklist IS NULL AND ? = ''))
        ''', (day, v_key, score, blacklist, blacklist))
        
        if not cur.fetchone():
            cur.execute('''
                INSERT INTO voice_evaluations 
                (day_number, voice_key, voice_name, channel, topic, score, audience_feedback, voice_rules_added, review_notes, blacklist, case_study, gold_sample)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (day, v_key, v_name, channel, topic, score, feedback, rules, notes, blacklist, case_study, gold_sample))
            inserted_evals += 1

    conn.commit()
    conn.close()

    print(f"🎉 Đồng bộ hoàn tất! Đã hợp nhất an toàn {inserted_evals} bản ghi tri thức mới vào brain.db.")

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--import':
        import_json_to_db(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == '--export':
        export_db_to_json()
    else:
        print("Sử dụng:")
        print("  python scripts/sync_brain.py --export                  (Xuất dữ liệu brain.db ra JSON)")
        print("  python scripts/sync_brain.py --import [file_backup.json] (Nạp an toàn file JSON vào brain.db)")
