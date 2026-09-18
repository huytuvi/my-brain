#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script đồng bộ 2 chiều giữa SQLite brain.db và Thư mục Tài liệu Markdown (medical_knowledge/)
- Chế độ --export (mặc định): Xuất 349 bài y khoa từ brain.db ra các file .md có cấu trúc gọn gàng để con người đọc/sửa.
- Chế độ --import: Đọc các file .md trong medical_knowledge/ và cập nhật lại vào brain.db khi con người chỉnh sửa bài giảng.
"""

import os
import re
import sys
import sqlite3
import unicodedata

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "brain.db")
MD_DIR = os.path.join(BASE_DIR, "medical_knowledge")

def slugify(text):
    """Chuyển tiếng Việt có dấu thành chuỗi không dấu an toàn cho tên file."""
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = text.replace('đ', 'd').replace('Đ', 'D')
    text = re.sub(r'[^a-zA-Z0-9\s_-]', '', text)
    text = re.sub(r'[\s]+', '_', text).strip('_')
    return text[:60]

def export_db_to_md():
    """Xuất toàn bộ bản ghi từ medical_knowledge ra các file .md phân theo thư mục chương."""
    print("🚀 Bắt đầu xuất tri thức y khoa từ brain.db ra các file Markdown (.md)...")
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("""
        SELECT id, chapter_num, chapter_title, section_code, section_title, 
               anatomical_region, topic, german_terms, red_flags, indications, 
               techniques, content, source_file, german_title, content_de
        FROM medical_knowledge
        ORDER BY id ASC;
    """)
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("❌ Không có dữ liệu trong bảng medical_knowledge!")
        return

    os.makedirs(MD_DIR, exist_ok=True)

    folder_map = {
        1: "01_Lich_Su_Triet_Ly",
        2: "02_Co_Che_Hoat_Dong",
        3: "03_Chi_Dinh_Va_Red_Flags",
        6: "04_Cot_Song_HWS_BWS_LWS",
        7: "05_Xuong_Chau_ISG",
        8: "06_Chi_Tren",
        9: "07_Dau_Va_Khop_Thai_Duong_Ham_TMG",
        10: "08_Chi_Duoi",
        11: "09_Thuat_Ngu_Va_Tu_Viet_Tat"
    }

    count = 0
    for r in rows:
        chap_num = r["chapter_num"]
        folder_name = folder_map.get(chap_num, f"Chuong_{chap_num:02d}")
        chap_dir = os.path.join(MD_DIR, folder_name)
        os.makedirs(chap_dir, exist_ok=True)

        sec_code = r["section_code"] or f"muc_{r['id']:03d}"
        safe_topic = slugify(r["topic"])
        fname = f"{sec_code}_{safe_topic}.md"
        fpath = os.path.join(chap_dir, fname)

        # Tạo nội dung Markdown giàu cấu trúc
        md_lines = []
        md_lines.append(f"# {r['section_title']}\n")
        md_lines.append(f"- **ID Hệ Thống:** `{r['id']}`")
        md_lines.append(f"- **Chương:** {r['chapter_title']}")
        md_lines.append(f"- **Phân Vùng Giải Phẫu:** {r['anatomical_region']}")
        if r["german_terms"]:
            md_lines.append(f"- **Thuật Ngữ Đức - Latinh:** {r['german_terms']}")
        if r["source_file"]:
            md_lines.append(f"- **Tài Liệu Gốc:** `{r['source_file']}`")

        if r["red_flags"]:
            md_lines.append("\n> ⚠️ **CẢNH BÁO ĐỎ / CHỐNG CHỈ ĐỊNH (RED FLAGS):**\n> " + "\n> ".join(r["red_flags"].split("\n")))

        if r["indications"]:
            md_lines.append("\n### 🎯 Chỉ Định Điều Trị Lâm Sàng:\n" + r["indications"])

        if r["techniques"]:
            md_lines.append("\n### 👐 Kỹ Thuật Nắn Chỉnh / Thao Tác (HVLA):\n" + r["techniques"])

        md_lines.append("\n---\n\n### 📖 Nội Dung Chuyên Môn Chi Tiết:\n")
        md_lines.append(r["content"])

        if r["content_de"]:
            g_hdr = f"**{r['german_title']}**\n\n" if r["german_title"] else ""
            md_lines.append(f"\n---\n\n### 🇩🇪 Nguyên Văn Tiếng Đức (Originaltext - Henrik Simon):\n{g_hdr}{r['content_de']}")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines))
        count += 1

    # Tạo file README.md chỉ mục tổng
    readme_path = os.path.join(MD_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"""# KHO TRI THỨC Y KHOA CHIROPRACTIC — SIMON CENTER
*(Lehrbuch Chiropraktik - Henrik Simon)*

Thư mục này lưu trữ toàn bộ **{count} khối tri thức y khoa chuyên sâu** đã được bóc tách và phân loại.
Các file Markdown tại đây là **Bản Gốc Dành Cho Con Người** để đọc, kiểm duyệt, bổ sung ca lâm sàng và cập nhật bài giảng.

## Cấu Trúc Các Thư Mục Chương:
1. `01_Lich_Su_Triet_Ly/`: Lịch sử, triết lý, trường phái nắn chỉnh cột sống quốc tế.
2. `02_Co_Che_Hoat_Dong/`: Cơ sở sinh học, hiện tượng Subluxation/Blockierung, cơ chế bọt khí Cavitation.
3. `03_Chi_Dinh_Va_Red_Flags/`: Chỉ định và Ranh giới Đỏ (Chống chỉ định tuyệt đối & tương đối).
4. `04_Cot_Song_HWS_BWS_LWS/`: Cột sống cổ C1-C7, ngực Th1-Th12, thắt lưng L1-L5 và đĩa đệm.
5. `05_Xuong_Chau_ISG/`: Khớp cùng chậu, xương cùng, kỹ thuật chân ngắn (PI) và chân dài (AS).
6. `06_Chi_Tren/`: Khớp vai, khuỷu, cổ tay Carpus, các khớp bàn ngón tay.
7. `07_Dau_Va_Khop_Thai_Duong_Ham_TMG/`: Khớp thái dương hàm, trượt đĩa sụn, kỹ thuật xoang mũi.
8. `08_Chi_Duoi/`: Khớp háng, khớp gối, cổ chân, bàn chân.
9. `09_Thuat_Ngu_Va_Tu_Viet_Tat/`: Bảng đối chiếu thuật ngữ Đức - Latinh - Việt.

---
*Mọi chỉnh sửa tại các file .md sẽ được đồng bộ ngược lại vào `brain.db` bằng lệnh:*
`python3 scripts/sync_knowledge_md.py --import`
""")

    print(f"🎉 Đã xuất thành công {count} file .md vào thư mục: {MD_DIR}")

def import_md_to_db():
    """Đọc các file .md trong medical_knowledge/ và cập nhật lại vào brain.db khi con người sửa."""
    print("🔄 Bắt đầu đọc các file .md và đồng bộ cập nhật vào brain.db...")
    if not os.path.exists(MD_DIR):
        print(f"❌ Thư mục {MD_DIR} không tồn tại!")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    updated = 0
    for root, _, files in os.walk(MD_DIR):
        for f in files:
            if f.endswith(".md") and f != "README.md":
                fpath = os.path.join(root, f)
                with open(fpath, "r", encoding="utf-8") as file:
                    content = file.read()

                # Trích xuất ID hệ thống nếu có
                id_match = re.search(r"\- \*\*ID Hệ Thống:\*\* `(\d+)`", content)
                if id_match:
                    item_id = int(id_match.group(1))
                    
                    # Tách phần nội dung chi tiết
                    content_parts = content.split("### 📖 Nội Dung Chuyên Môn Chi Tiết:\n")
                    if len(content_parts) > 1:
                        detail_text = content_parts[1].strip()
                        cur.execute("UPDATE medical_knowledge SET content = ? WHERE id = ?;", (detail_text, item_id))
                        updated += 1

    conn.commit()
    conn.close()
    print(f"✅ Đã đồng bộ cập nhật {updated} bài giảng từ Markdown vào brain.db!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--import":
        import_md_to_db()
    else:
        export_db_to_md()
