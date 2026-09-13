# Handoff Documentation

Sổ bàn giao trạng thái làm việc giữa các AI Agent (Antigravity ↔ Claude Code ↔ Cursor).

## Current Status
- **Trạng thái hiện tại**: Đã hoàn thành khởi tạo database SQLite `brain.db` và nạp dữ liệu mẫu ban đầu.
- **Agent thực hiện gần nhất**: Google Antigravity.
- **Thời gian**: 2026-09-13.

## What was completed
- Tạo script `scripts/create_db.py` hỗ trợ cơ chế idempotent.
- Tạo database SQLite `brain.db` tại thư mục gốc của project.
- Thiết lập 3 bảng: `knowledge`, `business`, `brand_voice`.
- Nạp 2 dòng dữ liệu mẫu vào mỗi bảng.
- Chạy kiểm tra truy vấn SQLite3 xác nhận dữ liệu đã được ghi nhận.

## What was changed
- Thêm mới `scripts/create_db.py`.
- Thêm mới cơ sở dữ liệu `brain.db`.
- Cập nhật `CHANGELOG.md`, `TODO.md`, `HANDOFF.md`.

## Tests performed
- Chạy `sqlite3 brain.db ".tables"` -> Trả về đủ 3 bảng: `brand_voice`, `business`, `knowledge`.
- Chạy `SELECT` trên từng bảng -> Xác nhận dữ liệu mẫu đã hiển thị chính xác.
- Chạy lại script `create_db.py` lần 2 -> Đảm bảo tính idempotent, không bị nhân đôi dữ liệu.

## Current state
- Database sẵn sàng để tiếp nhận Brand Voice và dữ liệu thực tế từ người dùng.

## Next task
- Thu thập Brand Voice thực tế từ người dùng (giọng điệu, từ yêu thích, từ kiêng kỵ, đối tượng đọc, bài viết mẫu).
- Nạp Brand Voice vào bảng `brand_voice` trong `brain.db`.
- Thực hiện sinh bài viết Facebook tự động và xuất ra file `post.txt` (và `output/post.txt`).

## Important decisions
- Giữ nguyên thiết kế bảng với cấu trúc 4 cột cơ bản (`id`, `title`, `content`, `created_at`) theo đúng chuẩn yêu cầu đề bài.
- Lưu trữ bài viết xuất ra ở cả thư mục gốc (`post.txt`) và thư mục `output/` để vừa tương thích SOP gốc vừa giữ cấu trúc dự án sạch sẽ.

## Known issues
- Không có.

## Instructions for next agent
- Đọc các bản ghi trong bảng `brand_voice` từ `brain.db`.
- Dựa trên phong cách này để sinh bài viết theo chủ đề mà người dùng chỉ định.
- Lưu bài viết vào `post.txt` và `output/post.txt`.
