# Handoff Documentation

Sổ bàn giao trạng thái làm việc giữa các AI Agent (Antigravity ↔ Claude Code ↔ Cursor).

## Current Status
- **Trạng thái hiện tại**: Đã nạp và huấn luyện thành công Brand Voice Simon Center (2 Giọng: Tư vấn 1-1 & Giảng học thuật) vào database `brain.db`.
- **Agent thực hiện gần nhất**: Google Antigravity.
- **Thời gian**: 2026-09-13.

## What was completed
- Lưu trữ file Brand Voice gốc tại `data/brand_voice/simon_center_brand_voice.md`.
- Cập nhật bảng `brand_voice` trong `brain.db` với 4 module:
  1. Nền tảng chung & Ranh giới Y khoa (Phần 0: Bốn chữ KHÔNG).
  2. Giọng 1: Tư vấn & Chuyên khoa (Hong Van + Gabor Maté + BS Trần Văn Phúc).
  3. Giọng 2: Giảng kiến thức học thuật (Doctor Mike + Elon Musk).
  4. Quy tắc chọn giọng & Checklist kiểm duyệt 6 điểm.
- Cập nhật thông tin nhận diện Simon Center vào bảng `business`.

## Tests performed
- Truy vấn SQLite `SELECT id, title FROM brand_voice` -> Xác nhận toàn bộ 4 module Brand Voice đã được lưu trữ hoàn chỉnh.
- Kiểm tra tính toàn vẹn của dữ liệu trong database `brain.db`.

## Current state
- Database `brain.db` đã mang đầy đủ trí tuệ và linh hồn thương hiệu của Simon Center.
- Sẵn sàng để thực hiện bước test viết bài ra file `post.txt` và `output/post.txt`.

## Next task
- Nhận chủ đề bài viết từ người dùng.
- AI đọc nội dung từ `brand_voice` trong `brain.db`, chọn giọng phù hợp (Giọng 1 hoặc Giọng 2) và tuân thủ tuyệt đối ranh giới y khoa.
- Viết bài và xuất file ra `post.txt` và `output/post.txt`.
- Chuẩn bị nội dung hoàn tất bài nộp SOP Day 5.

## Instructions for next agent
- Khi nhận yêu cầu viết bài, bắt buộc truy vấn bảng `brand_voice` trong `brain.db`.
- Luôn kiểm tra 6 tiêu chí checklist trong module 4 trước khi xuất bản nội dung y khoa.
