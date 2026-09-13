# Changelog

Tất cả những thay đổi quan trọng của project sẽ được ghi lại trong tài liệu này.

## [Unreleased]
- Chuẩn bị nạp Brand Voice thực tế từ người dùng.
- Sinh bài viết Facebook post mẫu theo Brand Voice.

## [0.3.0] - 2026-09-13
### Added
- Đào tạo và nạp toàn bộ Brand Voice chuẩn của Simon Center vào `brain.db`.
- Thiết lập 2 giọng văn chuyên biệt:
  + Giọng 1: Tư vấn & Chuyên khoa (thấu cảm, lắng nghe theo tinh thần Hong Van + Gabor Maté + BS Trần Văn Phúc).
  + Giọng 2: Giảng kiến thức học thuật & Đại chúng (tư duy nguyên lý gốc First Principles, relatable, fun theo Doctor Mike + Elon Musk).
- Thiết lập quy tắc chọn giọng và 6 tiêu chuẩn checklist kiểm duyệt y khoa (Bốn chữ KHÔNG).
- Lưu trữ tài liệu gốc tại `data/brand_voice/simon_center_brand_voice.md`.

## [0.2.0] - 2026-09-13
### Added
- Thêm script khởi tạo database `scripts/create_db.py`.
- Tạo cơ sở dữ liệu SQLite `brain.db` với 3 bảng: `knowledge`, `business`, `brand_voice`.
- Nạp 2 bản ghi mẫu cho mỗi bảng, hỗ trợ chạy lặp lại an toàn (idempotent).

## [0.1.0] - 2026-09-13
### Added
- Khởi tạo project Second Brain `my-brain`.
- Thiết lập hệ thống tài liệu: `README.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `TODO.md`, `HANDOFF.md`, `.gitignore`.
- Cấu hình quản lý phiên bản Git.
