import os
import sqlite3

base_dir = '/Users/huybui/Desktop/my-brain'
db_path = os.path.join(base_dir, 'brain.db')

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 1. Create table voice_evaluations with strict voice isolation
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
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert Day 1 evaluation for Voice 1 specifically
cur.execute("SELECT COUNT(*) FROM voice_evaluations WHERE day_number = 1 AND voice_key = 'voice1'")
if cur.fetchone()[0] == 0:
    cur.execute('''
        INSERT INTO voice_evaluations 
        (day_number, voice_key, voice_name, channel, topic, score, audience_feedback, voice_rules_added, review_notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        1,
        'voice1',
        'Giọng 1: Tư Vấn & Chuyên Khoa',
        'Facebook Cá Nhân',
        'Chúng ta đã học cách chịu đựng cơn đau giỏi đến mức nào?',
        9.0,
        'Khách khen bài ấm áp, thấu cảm, có 3 người nhắn tin hỏi link danh sách chờ.',
        'Nhấn mạnh lắng nghe trước khi khuyên, giữ ranh giới 4 chữ KHÔNG.',
        'Bài viết rất cảm xúc, chạm đúng tâm lý chịu đựng của dân văn phòng. CTA kéo vào form tự nhiên.'
    ))

conn.commit()
conn.close()
print("voice_evaluations table created with strict voice isolation!")
