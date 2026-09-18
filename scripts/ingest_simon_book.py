#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script nạp Giáo Trình Chỉnh Hình Học (Lehrbuch Chiropraktik) của Henrik Simon
từ 9 file Word (.docx) tại Desktop/Chiro_course/Simon_book vào brain.db.

Lưu trữ theo chuẩn Y Khoa Chuyên Sâu:
1. Bảng `medical_knowledge`: Cấu trúc phân loại theo phân vùng giải phẫu, chỉ định, chống chỉ định (Red Flags), kỹ thuật HVLA, thuật ngữ Đức-Latinh.
2. Bảng `knowledge`: Định dạng Markdown chuẩn y khoa đồng bộ tự động với sync_brain.py.
3. Bảng `medical_knowledge_fts`: Full-Text Search (FTS5) để tìm kiếm cực nhanh trong 0.001 giây.
"""

import os
import re
import glob
import sqlite3
import zipfile
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "brain.db")
BOOK_DIR = "/Users/huybui/Desktop/Chiro_course/Simon_book"

def extract_paragraphs_from_docx(docx_path):
    """Trích xuất danh sách đoạn văn từ file .docx bằng zipfile & ElementTree."""
    with zipfile.ZipFile(docx_path) as docx:
        tree = ET.fromstring(docx.read("word/document.xml"))
        namespaces = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        paras = []
        for p in tree.iterfind(".//w:p", namespaces):
            texts = [node.text for node in p.iterfind(".//w:t", namespaces) if node.text]
            if texts:
                t = "".join(texts).strip()
                if t:
                    paras.append(t)
        return paras

def detect_anatomical_region(section_title, content_text):
    """Phân loại phân vùng giải phẫu dựa trên tiêu đề và nội dung."""
    t_lower = (section_title + " " + content_text[:300]).lower()
    
    if any(k in t_lower for k in ["hws", "cổ", "cervical", "đốt cổ", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "động mạch đốt sống", "arteria vertebralis"]):
        return "Cột sống cổ (HWS / Cervical)"
    elif any(k in t_lower for k in ["bws", "ngực", "thorakal", "th1", "th2", "th3", "th4", "th5", "th6", "th7", "th8", "th9", "th10", "th11", "th12", "sườn", "costae"]):
        return "Cột sống ngực & Lồng ngực (BWS / Thoracic)"
    elif any(k in t_lower for k in ["lws", "thắt lưng", "lumbal", "l1", "l2", "l3", "l4", "l5", "đĩa đệm", "thoát vị", "thần kinh tọa", "ischiadicus"]):
        return "Cột sống thắt lưng (LWS / Lumbar)"
    elif any(k in t_lower for k in ["chậu", "becken", "isg", "cùng chậu", "iliosakral", "sacrum", "xương cùng", "xương cụt", "ilium", "chân ngắn", "chân dài"]):
        return "Xương chậu & Khớp cùng chậu (Becken / ISG / Pelvis)"
    elif any(k in t_lower for k in ["tmg", "thái dương hàm", "hàm", "kiefer", "cranium", "xoang", "đầu"]):
        return "Đầu & Khớp thái dương hàm (TMG / Cranium / TMJ)"
    elif any(k in t_lower for k in ["chi trên", "tay", "cổ tay", "vai", "khuỷu", "schulter", "hand", "carpus", "ngón tay"]):
        return "Chi trên (Vai, Khuỷu, Cổ tay, Bàn tay)"
    elif any(k in t_lower for k in ["chi dưới", "chân", "khớp háng", "gối", "knie", "cổ chân", "bàn chân", "fuß", "hallux"]):
        return "Chi dưới (Háng, Gối, Cổ chân, Bàn chân)"
    elif any(k in t_lower for k in ["chống chỉ định", "red flags", "chỉ định", "cảnh báo đỏ", "tai biến", "an toàn"]):
        return "Chỉ định & Ranh giới An toàn Y khoa (Red Flags / Safety)"
    else:
        return "Nguyên lý Cơ sinh học & Thuật ngữ (Biomechanics & Philosophy)"

def extract_red_flags(content_text):
    """Trích xuất các cảnh báo đỏ / chống chỉ định nếu có trong đoạn."""
    red_flag_triggers = ["chống chỉ định", "tuyệt đối không", "cấm nắn", "nguy cơ", "tai biến", "red flags", "contraindication", "rách bao xơ", "loãng xương nặng", "gãy xương", "u tủy"]
    paras = content_text.split("\n")
    flagged = []
    for p in paras:
        if any(trig in p.lower() for trig in red_flag_triggers):
            flagged.append(p.strip())
    return "\n• ".join(flagged[:4]) if flagged else None

def extract_indications(content_text):
    """Trích xuất chỉ định điều trị nếu có trong đoạn."""
    ind_triggers = ["chỉ định", "triệu chứng", "thích hợp", "chữa trị", "điều trị", "giảm đau", "chèn ép"]
    paras = content_text.split("\n")
    inds = []
    for p in paras:
        if any(trig in p.lower() for trig in ind_triggers) and len(p) > 20:
            inds.append(p.strip())
    return "\n• ".join(inds[:3]) if inds else None

def extract_techniques(content_text):
    """Trích xuất kỹ thuật nắn HVLA nếu có trong đoạn."""
    tech_triggers = ["kỹ thuật", "hvla", "điểm tiếp xúc", "tư thế bệnh nhân", "tư thế người nắn", "hướng lực", "vector", "thrust", "body drop", "tiếp xúc xương"]
    paras = content_text.split("\n")
    techs = []
    for p in paras:
        if any(trig in p.lower() for trig in tech_triggers) and len(p) > 20:
            techs.append(p.strip())
    return "\n• ".join(techs[:3]) if techs else None

def extract_german_terms(content_text):
    """Trích xuất các thuật ngữ tiếng Đức / Latinh trong ngoặc đơn."""
    terms = re.findall(r"\(([A-Za-zäöüßÄÖÜ\s\-\/]{3,35})\)", content_text)
    valid_terms = []
    for t in terms:
        t_clean = t.strip()
        if not t_clean.isdigit() and len(t_clean) > 2:
            valid_terms.append(t_clean)
    return ", ".join(list(set(valid_terms))[:8]) if valid_terms else None

def setup_database_tables(conn):
    """Tạo cấu trúc bảng chuyên dụng cho Y khoa trong SQLite brain.db."""
    cur = conn.cursor()
    
    # 1. Bảng medical_knowledge chuyên sâu
    cur.execute("""
        CREATE TABLE IF NOT EXISTS medical_knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapter_num INTEGER,
            chapter_title TEXT NOT NULL,
            section_code TEXT,
            section_title TEXT NOT NULL,
            anatomical_region TEXT NOT NULL,
            topic TEXT NOT NULL,
            german_terms TEXT,
            red_flags TEXT,
            indications TEXT,
            techniques TEXT,
            content TEXT NOT NULL,
            source_file TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    cur.execute("CREATE INDEX IF NOT EXISTS idx_med_region ON medical_knowledge(anatomical_region);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_med_topic ON medical_knowledge(topic);")

    # 2. Bảng FTS5 để Full-Text Search siêu tốc
    cur.execute("DROP TABLE IF EXISTS medical_knowledge_fts;")
    cur.execute("""
        CREATE VIRTUAL TABLE medical_knowledge_fts USING fts5(
            section_title,
            anatomical_region,
            topic,
            german_terms,
            red_flags,
            content,
            content='medical_knowledge',
            content_rowid='id'
        );
    """)
    
    # 3. Đảm bảo bảng knowledge chuẩn vẫn tồn tại
    cur.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    conn.commit()

def process_and_ingest():
    print("🚀 Bắt đầu quá trình nạp Giáo Trình Y Khoa Chuyên Sâu (Henrik Simon)...")
    
    files = sorted(glob.glob(os.path.join(BOOK_DIR, "*.docx")))
    if not files:
        print(f"❌ Không tìm thấy file .docx nào trong {BOOK_DIR}")
        return

    conn = sqlite3.connect(DB_PATH)
    setup_database_tables(conn)
    cur = conn.cursor()

    # Xóa dữ liệu cũ của sách trong medical_knowledge & knowledge
    cur.execute("DELETE FROM medical_knowledge;")
    cur.execute("DELETE FROM knowledge WHERE title LIKE '[Y Khoa - %';")
    conn.commit()

    sec_pattern = re.compile(r"^(?:CHƯƠNG|Chương|PHẦN|Phần|\d+\.\d+|\d+\.\d+\.\d+|\d+\.\d+\.\d+\.\d+)\s*(.*)")
    
    total_chunks = 0
    part_mapping = {
        "Phan1": (1, "Chương 1: Lịch Sử, Triết Lý & Bối Cảnh Chiropractic"),
        "Phan2": (2, "Chương 2: Cơ Sở Về Cơ Chế Hoạt Động Của Chỉnh Hình Học"),
        "Phan3": (3, "Chương 3–5: Chỉ Định, Chống Chỉ Định (Red Flags) & Khám Lâm Sàng"),
        "Phan4": (6, "Chương 6: Cột Sống (HWS, BWS, LWS & Kỹ Thuật Nắn HVLA)"),
        "Phan5": (7, "Chương 7: Xương Chậu (Becken & Khớp Cùng Chậu ISG)"),
        "Phan6": (8, "Chương 8: Chi Trên (Vai, Khuỷu, Cổ Tay, Bàn Tay)"),
        "Phan7": (9, "Chương 9: Đầu & Khớp Thái Dương Hàm (TMG / Cranium)"),
        "Phan8": (10, "Chương 10: Chi Dưới (Háng, Gối, Cổ Chân, Bàn Chân)"),
        "Phan9": (11, "Chương 11–12: Bảng Từ Viết Tắt & Thuật Ngữ Đức - Latinh - Việt")
    }

    for fpath in files:
        fname = os.path.basename(fpath)
        
        chap_num = 1
        chap_title = "Giáo Trình Chỉnh Hình Học"
        for key, val in part_mapping.items():
            if key in fname:
                chap_num, chap_title = val
                break

        print(f"\n📂 Đang xử lý: {fname} -> {chap_title}...")
        paras = extract_paragraphs_from_docx(fpath)
        
        current_sec = f"Giới thiệu {chap_title}"
        current_content = []
        
        for p in paras:
            is_heading = False
            p_strip = p.strip()
            
            if len(p_strip) < 130:
                if sec_pattern.match(p_strip) or p_strip.startswith("CHƯƠNG") or p_strip.startswith("Chương") or p_strip.startswith("PHẦN"):
                    is_heading = True
                elif re.match(r"^\d+\.\s+[A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰÝỲỶỸỴ]", p_strip):
                    is_heading = True

            if is_heading:
                if current_content:
                    text_block = "\n\n".join(current_content).strip()
                    if len(text_block) > 60:
                        save_chunk(cur, chap_num, chap_title, current_sec, text_block, fname)
                        total_chunks += 1
                current_sec = p_strip
                current_content = []
            else:
                current_content.append(p_strip)

        if current_content:
            text_block = "\n\n".join(current_content).strip()
            if len(text_block) > 60:
                save_chunk(cur, chap_num, chap_title, current_sec, text_block, fname)
                total_chunks += 1

    # Đồng bộ sang bảng FTS5
    cur.execute("""
        INSERT INTO medical_knowledge_fts(rowid, section_title, anatomical_region, topic, german_terms, red_flags, content)
        SELECT id, section_title, anatomical_region, topic, german_terms, red_flags, content FROM medical_knowledge;
    """)

    conn.commit()
    conn.close()

    print("\n" + "=" * 80)
    print(f"🎉 HOÀN THÀNH NẠP GIÁO TRÌNH Y KHOA VÀO BRAIN.DB!")
    print(f"✅ Đã bóc tách và lưu trữ thành công: {total_chunks} khối tri thức chuyên sâu.")
    print("=" * 80)

def save_chunk(cur, chap_num, chap_title, sec_title, content, fname):
    """Phân tích và lưu một khối tri thức vào database."""
    region = detect_anatomical_region(sec_title, content)
    red_flags = extract_red_flags(content)
    indications = extract_indications(content)
    techniques = extract_techniques(content)
    german_terms = extract_german_terms(content)

    code_match = re.match(r"^(\d+(?:\.\d+)*)\s*(.*)", sec_title)
    if code_match:
        sec_code = code_match.group(1)
        topic_name = code_match.group(2).strip() or sec_title
    else:
        sec_code = ""
        topic_name = sec_title

    # 1. Lưu vào bảng medical_knowledge
    cur.execute("""
        INSERT INTO medical_knowledge 
        (chapter_num, chapter_title, section_code, section_title, anatomical_region, topic, german_terms, red_flags, indications, techniques, content, source_file)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (chap_num, chap_title, sec_code, sec_title, region, topic_name, german_terms, red_flags, indications, techniques, content, fname))

    # 2. Đồng thời lưu vào bảng knowledge chuẩn dạng Markdown để tương thích mọi công cụ
    md_content = f"""# {sec_title}
**Chương:** {chap_title}  
**Phân vùng giải phẫu:** {region}  
"""
    if german_terms:
        md_content += f"**Thuật ngữ Đức - Latinh:** {german_terms}\n"
    if red_flags:
        md_content += f"\n> ⚠️ **CẢNH BÁO ĐỎ / CHỐNG CHỈ ĐỊNH (RED FLAGS):**\n• {red_flags}\n"
    if indications:
        md_content += f"\n**Chỉ định điều trị:**\n• {indications}\n"
    if techniques:
        md_content += f"\n**Kỹ thuật nắn HVLA / Thao tác:**\n• {techniques}\n"

    md_content += f"\n---\n\n### Nội dung lâm sàng:\n{content}"

    full_knowledge_title = f"[Y Khoa - Chương {chap_num}] {sec_title[:80]}"
    cur.execute("""
        INSERT INTO knowledge (title, content)
        VALUES (?, ?);
    """, (full_knowledge_title, md_content))

if __name__ == "__main__":
    process_and_ingest()
