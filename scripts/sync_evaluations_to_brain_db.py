#!/usr/bin/env python3
import json
import sqlite3
import sys
import os

def sync_evaluations_from_json(json_path, db_path):
    if not os.path.exists(json_path):
        print(f'File khong ton tai: {json_path}')
        return False
    if not os.path.exists(db_path):
        print(f'Database khong ton tai: {db_path}')
        return False

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    evaluations = data.get('evaluations', [])
    if not evaluations:
        print('Khong tim thay danh sach evaluations trong file JSON.')
        return False

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    inserted = 0
    updated = 0

    for ev in evaluations:
        day_num = ev.get('day', 1)
        v_key = ev.get('voiceKey', 'voice1')
        v_name = ev.get('voiceName', 'Giong 1')
        topic = ev.get('topic', 'Cham soc cot song')
        score = ev.get('score', 9.0)
        feedback = ev.get('feedback', '')
        rules = ev.get('rules', '')
        blacklist = ev.get('blacklist', '')
        case_study = ev.get('caseStudy', '')
        gold_sample = ev.get('goldSample', '')

        cur.execute('SELECT id FROM voice_evaluations WHERE day_number=? AND voice_key=? AND topic=?', (day_num, v_key, topic))
        row = cur.fetchone()
        if row:
            cur.execute('UPDATE voice_evaluations SET score=?, audience_feedback=?, voice_rules_added=?, blacklist=?, case_study=?, gold_sample=? WHERE id=?', (score, feedback, rules, blacklist, case_study, gold_sample, row[0]))
            updated += 1
        else:
            cur.execute('INSERT INTO voice_evaluations (day_number, voice_key, voice_name, topic, score, audience_feedback, voice_rules_added, blacklist, case_study, gold_sample) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (day_num, v_key, v_name, topic, score, feedback, rules, blacklist, case_study, gold_sample))
            inserted += 1

    conn.commit()
    conn.close()
    print(f'Da dong bo vao {db_path}: Them moi {inserted}, Cap nhat {updated}')
    return True

if __name__ == '__main__':
    json_p = sys.argv[1] if len(sys.argv) > 1 else 'brain_backup.json'
    db_p = sys.argv[2] if len(sys.argv) > 2 else '/Users/huybui/Desktop/my-brain/brain.db'
    sync_evaluations_from_json(json_p, db_p)
