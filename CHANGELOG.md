# Changelog

Tất cả những thay đổi quan trọng của project sẽ được ghi lại trong tài liệu này.

## [Unreleased]
- Chuẩn bị nạp Brand Voice thực tế từ người dùng.
- Sinh bài viết Facebook post mẫu theo Brand Voice.

## [0.5.0] - 2026-09-14
### Added
- Đào tạo và cập nhật trọn bộ **3 Tone Brand Voice** vào `brain.db`:
  + Giọng 1: Tư vấn & Chuyên khoa (thấu cảm, đồng hành 1-1).
  + Giọng 2: Giảng kiến thức học thuật & Đại chúng (First Principles, lôi cuốn).
  + Giọng 3: Sale & Chốt deal chuẩn Y đức ('Bán hàng có tâm', Feel-Felt-Found, sức khỏe trước doanh số).
- Thêm bài viết mẫu thực tế cho Giọng 3: Xử lý từ chối về chi phí liệu trình và chốt buổi đánh giá 1-1.
- Cập nhật toàn bộ file tài liệu nguồn `simon_center_brand_voice.md`, `post.txt` và sổ bàn giao `HANDOFF.md`.

## [0.4.0] - 2026-09-13
### Added
- Hoàn thành bài test sinh nội dung tự động từ `brand_voice` trong `brain.db`.
- Tạo thành công 2 bài viết mẫu chuyên nghiệp:
  + Bài 1 (Giọng 1: Tư vấn 1-1 thấu cảm): 'Thoát vị đĩa đệm: Có phải cứ đau là phải nghĩ đến phẫu thuật?'.
  + Bài 2 (Giọng 2: Giảng học thuật & đại chúng - First Principles): 'Tiếng kêu lục khục/rắc ở cổ và lưng: Khi nào là bình thường, khi nào là báo động?'.
- Xuất dữ liệu ra file `post.txt` tại thư mục gốc và thư mục `output/`.
- Kiểm tra toàn diện checklist 6 điểm chuẩn y khoa (tuân thủ Bốn chữ KHÔNG, sạch thương mại, có cảnh báo tham khảo).

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
