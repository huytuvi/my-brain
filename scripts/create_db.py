import sqlite3
import os
from datetime import datetime

def init_db():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, 'brain.db')
    print(f"Connecting to database at: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Create table: knowledge
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 2. Create table: business
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS business (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 3. Create table: brand_voice
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS brand_voice (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Insert sample data idempotently (check if empty or already has records)
    cursor.execute("SELECT COUNT(*) FROM knowledge")
    if cursor.fetchone()[0] == 0:
        knowledge_samples = [
            ("Nguyên lý Pareto 80/20", "80% kết quả đến từ 20% nguyên nhân cốt lõi. Trong kinh doanh và sáng tạo nội dung, tập trung vào 20% hoạt động tạo ra giá trị cao nhất thay vì dàn trải."),
            ("Mô hình AI-First Workflow", "Thay vì để con người làm từ đầu, hãy để AI tạo bản nháp đầu tiên, con người đóng vai trò biên tập, kiểm duyệt và cá nhân hóa giọng điệu.")
        ]
        cursor.executemany("INSERT INTO knowledge (title, content) VALUES (?, ?)", knowledge_samples)
        print("Inserted sample data into knowledge table.")

    cursor.execute("SELECT COUNT(*) FROM business")
    if cursor.fetchone()[0] == 0:
        business_samples = [
            ("Sản phẩm cốt lõi: Khóa học AI Coding", "Chương trình đào tạo giúp người không chuyên công nghệ ứng dụng AI Coding Agent (Antigravity, Claude Code) để tự động hóa công việc và xây dựng giải pháp số."),
            ("Khách hàng mục tiêu", "Chủ doanh nghiệp vừa và nhỏ, solopreneurs, quản lý, người làm nội dung mong muốn tăng năng suất x5-x10 lần bằng AI.")
        ]
        cursor.executemany("INSERT INTO business (title, content) VALUES (?, ?)", business_samples)
        print("Inserted sample data into business table.")

    cursor.execute("SELECT COUNT(*) FROM brand_voice")
    if cursor.fetchone()[0] == 0:
        brand_voice_samples = [
            ("Định vị phong cách viết", "Thẳng thắn, gãy gọn, logic, giàu tính thực chiến. Không dùng từ ngữ sáo rỗng, không hoa mỹ rườm rà. Ưu tiên đi thẳng vào bản chất vấn đề."),
            ("Từ khóa yêu thích & cấu trúc", "Hay dùng các cụm: 'thực tế là', 'điểm quan trọng là', 'đơn giản thôi', 'bản chất vấn đề'. Cấu trúc bài viết luôn có luận điểm rõ ràng, dẫn chứng và hành động cụ thể.")
        ]
        cursor.executemany("INSERT INTO brand_voice (title, content) VALUES (?, ?)", brand_voice_samples)
        print("Inserted sample data into brand_voice table.")

    conn.commit()
    conn.close()
    print("Database initialization completed successfully!")

if __name__ == '__main__':
    init_db()
