# ARCHITECTURE & SYSTEM DESIGN: SECOND BRAIN (SIMON CENTER)

> **Triết lý cốt lõi:**
> **"One Brain. Many Sources. Many Knowledge Types. Many Modes. Many Voices. One Safety Layer."**
> *(Một bộ não — nhiều nguồn kiến thức — nhiều loại kiến thức — nhiều chế độ sử dụng — nhiều phong cách giao tiếp — một lớp an toàn chung.)*

---

## 1. TỔNG QUAN HỆ THỐNG & KHẢ NĂNG TÍCH HỢP APP / CHATBOT

Hệ thống Second Brain được thiết kế theo tư duy **Module hóa (Modular Architecture)**, cho phép:
1. **Dùng làm Backend cho App / Chatbot tư vấn khách hàng (Patient Mode)**: Tự động dùng Voice 1, áp dụng ranh giới y khoa (Bốn chữ KHÔNG), hướng dẫn bước tiếp theo và cảnh báo cờ đỏ đi khám trực tiếp.
2. **Dùng làm Trợ giảng AI / Chuyên gia đồng hành cho lớp học (Student Mode)**: Tự động dùng Voice 2, giải thích cơ chế theo nguyên lý gốc (First Principles), đập tan lầm tưởng bằng khoa học, ra đề quiz, đánh giá câu trả lời của học viên.
3. **Dùng làm Cố vấn vận hành nội bộ (Internal Mode)**: Tra cứu quy trình SOP, đào tạo nhân sự phòng khám, bảng giá và chính sách dịch vụ.
4. **Dùng làm Nghiên cứu chuyên sâu (Research Mode)**: Tra cứu sách chuyên ngành Chiropractic, trích dẫn bài báo khoa học, đối chiếu bằng chứng y văn.

---

## 2. KIẾN TRÚC ĐA TẦNG (MULTI-LAYER ARCHITECTURE)

```mermaid
graph TD
    Client[Người dùng / Học viên / Bệnh nhân / App UI] --> Router[AI Router & Intent Detector]
    
    subgraph Core Brain Engine [CƠ CHẾ BỘ NÃO DUY NHẤT]
        Router --> Safety[TẦNG AN TOÀN TOÀN CỤC: Medical Safety & Global Rules]
        Safety --> ModeSelect{Chọn Mode & Voice}
        
        ModeSelect -->|Bệnh nhân hỏi triệu chứng| Voice1[Voice 1: Consultation - Thấu cảm, đồng hành]
        ModeSelect -->|Học viên hỏi cơ chế / học thuật| Voice2[Voice 2: Teaching - First Principles, lôi cuốn]
        ModeSelect -->|Nhân sự hỏi vận hành| Voice3[Voice 3: Internal SOP / Business]
        
        Voice1 --> RAG[Knowledge Retrieval & Context Generator]
        Voice2 --> RAG
        Voice3 --> RAG
        
        RAG --> DB[(Database: brain.db SQLite / Future Vector Index)]
    end
    
    Core Brain Engine --> Response[Câu trả lời chuẩn y khoa & đúng giọng]
```

---

## 3. MÔ HÌNH DỮ LIỆU: TIẾN HÓA KHÔNG CẦN "ĐẬP ĐI XÂY LẠI"

Để tương thích hoàn hảo từ giai đoạn học tập hiện tại (Day 5) đến hệ thống Production hoàn chỉnh trong tương lai, mô hình dữ liệu phát triển theo lộ trình:

### Giai đoạn hiện tại (Level 1 - MVP): Đang chạy trên `brain.db`
Giữ cấu trúc đơn giản, nhẹ, chuẩn đề bài nhưng phân định rõ logic qua các bản ghi:
- **`brand_voice`**:
  - `global_rules & safety_rules`: Lớp an toàn y khoa bất biến (Bốn chữ KHÔNG).
  - `voice_consultation`: Hồ sơ giọng 1 (Tư vấn 1-1).
  - `voice_teaching`: Hồ sơ giọng 2 (Giảng học thuật).
  - `voice_selection`: Logic điều hướng và checklist 6 điểm.
- **`knowledge`**: Kiến thức y khoa, bài học, insights lâm sàng.
- **`business`**: Dữ liệu định vị Simon Center, dịch vụ, sứ mệnh.

### Giai đoạn mở rộng (Level 2 - Level 5): Nâng cấp thêm bảng mà KHÔNG phá hủy dữ liệu cũ
- Bổ sung bảng `sources` (lưu nguồn gốc: Sách Chiro, transcript ghi âm, bài báo y khoa, tác giả, mức độ bằng chứng).
- Bổ sung bảng `knowledge_chunks` liên kết với `sources` để phục vụ Semantic Search / Vector Embedding (RAG).
- Bổ sung bảng `voice_profiles` chuyên biệt để mở rộng thêm Voice 3 (Marketing), Voice 4 (Học thuật chuyên sâu).

---

## 4. QUY TRÌNH TIẾP NHẬN DỮ LIỆU ĐA NGUỒN (INGESTION PIPELINE TƯƠNG LAI)

1. **Sách & Tài liệu (PDF, DOCX, TXT)**:
   `Tài liệu thô` → `Trích xuất văn bản` → `Làm sạch` → `Chia nhỏ (Chunking)` → `Gán Metadata nguồn` → `Vector Embeddings` → `RAG`.
2. **Bản ghi âm bài giảng / Phỏng vấn chuyên gia**:
   `Audio` → `Speech-to-Text` → `Transcript gốc (bảo toàn)` → `Nhận diện diễn giả & chủ đề` → `Nạp Knowledge Base`.

---

## 5. NGUYÊN TẮC KỸ THUẬT: "SIMPLE NOW, EXTENSIBLE LATER"
1. Không over-engineer ở giai đoạn ban đầu; hoàn thành chắc chắn từng bước.
2. Một bộ não duy nhất, không tạo nhiều file .db riêng rẽ gây phân mảnh kiến thức.
3. Lớp bảo vệ an toàn y khoa là độc lập và luôn được kích hoạt trước khi bất kỳ câu trả lời nào được xuất ra.
