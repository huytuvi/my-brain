#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script nạp toàn văn sách gốc tiếng Đức (Lehrbuch Chiropraktik - Henrik Simon)
từ file EPUB tại Desktop/Chiro_course/Simon_book vào SQLite brain.db.

Tính năng:
1. Trích xuất toàn bộ 27 chương XHTML từ file EPUB.
2. Ghép nối song ngữ 1-1 với 349 khối tri thức tiếng Việt trong bảng `medical_knowledge` (thêm cột `german_title`, `content_de`).
3. Tạo bảng độc lập `german_knowledge` chứa toàn bộ 375+ mục tiếng Đức gốc.
4. Cập nhật bảng FTS5 `medical_knowledge_fts` hỗ trợ tìm kiếm song ngữ Đức - Việt.
5. Cập nhật bảng chuẩn `knowledge` kèm đoạn nguyên văn tiếng Đức.
"""

import os
import re
import zipfile
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "brain.db")
EPUB_PATH = "/Users/huybui/Desktop/Chiro_course/Simon_book/Lehrbuch Chiropraktik (German Edition)_nodrm.epub"

def extract_german_sections_from_epub(epub_path):
    """Bóc tách các mục tiếng Đức từ file EPUB kèm mã mục (section code) và tiêu đề."""
    print(f"📖 Đang đọc file EPUB: {epub_path}...")
    german_sections = []
    
    with zipfile.ZipFile(epub_path) as z:
        for i in range(7, 26):
            h = f"OEBPS/part{i:04d}.xhtml"
            try:
                raw = z.read(h).decode("utf-8", errors="ignore")
            except KeyError:
                continue

            # Xác định chương lớn từ tên file hoặc thẻ h1
            h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.IGNORECASE)
            chap_h1 = re.sub(r"<[^>]+>", "", h1_match.group(1)).strip().replace("\xa0", " ") if h1_match else ""

            # Tách theo các thẻ tiêu đề h1 -> h5
            tokens = re.split(r"(<h[1-5][^>]*>.*?</h[1-5]>)", raw, flags=re.DOTALL | re.IGNORECASE)
            current_h = chap_h1 or f"Kapitel Teil {i}"
            current_code = None
            current_text_parts = []

            for tok in tokens:
                h_match = re.match(r"<h[1-5][^>]*>(.*?)</h[1-5]>", tok, flags=re.DOTALL | re.IGNORECASE)
                if h_match:
                    if current_text_parts:
                        full_text = "\n\n".join(current_text_parts).strip()
                        if len(full_text) > 20:
                            german_sections.append({
                                "file": h,
                                "heading": current_h,
                                "code": current_code,
                                "text": full_text
                            })
                    
                    current_h = re.sub(r"<[^>]+>", "", h_match.group(1)).strip().replace("\xa0", " ")
                    code_m = re.match(r"^(\d+(?:\.\d+)*)", current_h)
                    current_code = code_m.group(1) if code_m else None
                    current_text_parts = []
                else:
                    # Lấy text sạch từ HTML token
                    clean = re.sub(r"<[^>]+>", " ", tok).strip()
                    clean = re.sub(r"\s+", " ", clean).replace("\xa0", " ")
                    if clean:
                        current_text_parts.append(clean)

            if current_text_parts:
                full_text = "\n\n".join(current_text_parts).strip()
                if len(full_text) > 20:
                    german_sections.append({
                        "file": h,
                        "heading": current_h,
                        "code": current_code,
                        "text": full_text
                    })

    print(f"✅ Đã trích xuất thành công {len(german_sections)} mục tiếng Đức từ file EPUB.")
    return german_sections

def update_database_with_german():
    if not os.path.exists(EPUB_PATH):
        print(f"❌ Không tìm thấy file EPUB tại: {EPUB_PATH}")
        return

    german_sections = extract_german_sections_from_epub(EPUB_PATH)
    
    # Tạo chỉ mục tra cứu theo section_code
    code_to_german = {}
    for g in german_sections:
        if g["code"]:
            code_to_german[g["code"]] = g
        # Lưu cả theo heading
        code_to_german[g["heading"]] = g

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. Thêm cột tiếng Đức vào bảng medical_knowledge nếu chưa có
    cur.execute("PRAGMA table_info(medical_knowledge);")
    columns = [col[1] for col in cur.fetchall()]
    if "content_de" not in columns:
        print("🔧 Đang thêm cột `content_de` và `german_title` vào bảng `medical_knowledge`...")
        cur.execute("ALTER TABLE medical_knowledge ADD COLUMN german_title TEXT;")
        cur.execute("ALTER TABLE medical_knowledge ADD COLUMN content_de TEXT;")
        conn.commit()

    # 2. Tạo bảng độc lập german_knowledge
    cur.execute("""
        CREATE TABLE IF NOT EXISTS german_knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section_code TEXT,
            german_heading TEXT NOT NULL,
            german_text TEXT NOT NULL,
            matched_vn_id INTEGER,
            epub_source TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    cur.execute("DELETE FROM german_knowledge;")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_ger_code ON german_knowledge(section_code);")

    # 3. Ghép nối song ngữ vào medical_knowledge
    cur.execute("SELECT id, section_code, section_title, content FROM medical_knowledge ORDER BY id ASC;")
    vn_rows = cur.fetchall()

    matched_count = 0
    for r in vn_rows:
        vn_id, sec_code, sec_title, vn_content = r
        matched_german = None

        if sec_code and sec_code in code_to_german:
            matched_german = code_to_german[sec_code]
        else:
            # Tìm mờ theo mã số xuất hiện trong tiêu đề
            code_match = re.search(r"\b(\d+\.\d+(?:\.\d+)*)\b", sec_title)
            if code_match and code_match.group(1) in code_to_german:
                matched_german = code_to_german[code_match.group(1)]

        if matched_german:
            matched_count += 1
            g_title = matched_german["heading"]
            g_text = matched_german["text"]
            cur.execute("""
                UPDATE medical_knowledge 
                SET german_title = ?, content_de = ? 
                WHERE id = ?;
            """, (g_title, g_text, vn_id))

    print(f"🎯 Đã ghép nối song ngữ thành công: {matched_count}/{len(vn_rows)} bài giảng y khoa!")

    # 4. Bơm vào bảng độc lập german_knowledge
    for g in german_sections:
        matched_vn_id = None
        if g["code"]:
            cur.execute("SELECT id FROM medical_knowledge WHERE section_code = ? LIMIT 1;", (g["code"],))
            row = cur.fetchone()
            if row:
                matched_vn_id = row[0]

        cur.execute("""
            INSERT INTO german_knowledge (section_code, german_heading, german_text, matched_vn_id, epub_source)
            VALUES (?, ?, ?, ?, ?);
        """, (g["code"], g["heading"], g["text"], matched_vn_id, g["file"]))

    # 5. Tái thiết lập FTS5 để hỗ trợ tìm kiếm song ngữ
    print("⚡ Đang cập nhật bảng chỉ mục FTS5 đa ngôn ngữ...")
    cur.execute("DROP TABLE IF EXISTS medical_knowledge_fts;")
    cur.execute("""
        CREATE VIRTUAL TABLE medical_knowledge_fts USING fts5(
            section_title,
            german_title,
            anatomical_region,
            topic,
            german_terms,
            red_flags,
            content,
            content_de,
            content='medical_knowledge',
            content_rowid='id'
        );
    """)
    cur.execute("""
        INSERT INTO medical_knowledge_fts(rowid, section_title, german_title, anatomical_region, topic, german_terms, red_flags, content, content_de)
        SELECT id, section_title, german_title, anatomical_region, topic, german_terms, red_flags, content, content_de FROM medical_knowledge;
    """)

    # 6. Cập nhật bảng knowledge chuẩn kèm phần tiếng Đức
    print("📝 Cập nhật bảng knowledge với đoạn nguyên văn tiếng Đức...")
    cur.execute("SELECT id, section_title, content, content_de, german_title FROM medical_knowledge WHERE content_de IS NOT NULL;")
    for row in cur.fetchall():
        med_id, sec_title, content_vn, content_de, g_title = row
        knowledge_title_like = f"%{sec_title[:40]}%"
        
        appendix_de = f"\n\n---\n\n### 🇩🇪 Nguyên Văn Tiếng Đức (Originaltext - Henrik Simon):\n**{g_title}**\n\n{content_de}"
        cur.execute("""
            UPDATE knowledge 
            SET content = content || ? 
            WHERE title LIKE ? AND content NOT LIKE '%Originaltext%';
        """, (appendix_de, knowledge_title_like))

    conn.commit()
    conn.close()

    print("\n" + "=" * 80)
    print("🎉 HOÀN THÀNH NẠP TOÀN VĂN TIẾNG ĐỨC VÀO BRAIN.DB!")
    print(f"✅ Đã nạp trọn vẹn: {len(german_sections)} mục tiếng Đức vào `german_knowledge`.")
    print(f"✅ Đã đồng bộ song ngữ 1-1 cho {matched_count} bài giảng y khoa trong `medical_knowledge`.")
    print("=" * 80)

if __name__ == "__main__":
    update_database_with_german()
