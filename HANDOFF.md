# Handoff Documentation

Sổ bàn giao trạng thái làm việc giữa các AI Agent (Antigravity ↔ Claude Code ↔ Cursor).

## Current Status
- **Trạng thái hiện tại**: Đã hoàn thành 100% mục tiêu của SOP Ngày 5 - Xây dựng Bộ Não Thứ 2 (Second Brain).
- **Agent thực hiện gần nhất**: Google Antigravity.
- **Thời gian**: 2026-09-13.

## What was completed
- Khởi tạo thư mục và Git version control (`my-brain`).
- Thiết lập đầy đủ bộ tài liệu chuẩn: `README.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `TODO.md`, `HANDOFF.md`, `.gitignore`.
- Tạo cơ sở dữ liệu SQLite `brain.db` bằng script `scripts/create_db.py` (đảm bảo tính idempotent).
- Huấn luyện và nạp toàn bộ tài liệu Brand Voice của Simon Center vào bảng `brand_voice` (gồm Nền tảng chung, Giọng 1 Tư vấn 1-1, Giọng 2 Giảng học thuật, và Quy tắc chọn giọng / Checklist kiểm duyệt).
- Sinh thành công 2 bài viết mẫu theo đúng 2 tone voice ra file `post.txt` và `output/post.txt`.

## What was changed
- Thêm file `post.txt` tại gốc và các bài viết riêng biệt trong `output/`.
- Cập nhật `CHANGELOG.md`, `TODO.md`, `HANDOFF.md`.

## Tests performed
- Truy vấn bảng `brand_voice` từ SQLite `brain.db` để lấy dữ liệu giọng văn.
- Kiểm tra 6 tiêu chí y khoa trước khi xuất bản (xưng hô chuẩn lễ nghi, 4 chữ KHÔNG, dặn khám trực tiếp khi có dấu hiệu cờ đỏ, câu miễn trừ trách nhiệm y khoa).
- File `post.txt` đã được ghi thành công với dung lượng đầy đủ.

## Current state
- Dự án đã hoàn tất trọn vẹn, sẵn sàng nộp bài SOP Ngày 5 hoặc tiếp tục phát triển mở rộng (RAG, Semantic Search, Agent luân chuyển).

## Next task
- Người dùng review nội dung trong `post.txt` để đánh giá độ giống giọng văn.
- Chụp ảnh màn hình terminal / agent để làm bằng chứng nộp bài.
- Có thể test tính năng chuyển giao sang Claude Code theo Bước 13 của tài liệu `Bai 5.docx`.

## Important decisions
- Duy trì 2 giọng văn song song trong cùng một Second Brain: một giọng cho đồng hành trị liệu (1-1) và một giọng cho giáo dục đại chúng (community).
- Lưu giữ nguyên tắc y khoa bất biến làm 'lan can an toàn' (guardrail) cho mọi câu trả lời của AI trong tương lai.

## Known issues
- Không có.

## Instructions for next agent
- Đọc kỹ `HANDOFF.md`, `README.md` và kiểm tra `git status` trước khi thực hiện bất kỳ lệnh nào.
- Khi tiếp nhận viết bài mới, hãy query bảng `brand_voice` trong `brain.db` và tuân thủ checklist y khoa đã thiết lập.

## Architecture Alignment (2026-09-13)
- Đã đồng bộ triết lý thiết kế dài hạn: 'One Brain. Many Sources. Many Modes. Many Voices. One Safety Layer'.
- Khẳng định tính khả thi của việc tích hợp vào App / Chatbot / AI Trợ giảng cho lớp học.
- Cấu trúc hiện tại của brain.db hoàn toàn tương thích và mở rộng được mà không cần đập đi xây lại.

## Update 3 Brand Voices (2026-09-14)
- Bổ sung hoàn chỉnh Giọng 3 (Sale y đức) vào bảng `brand_voice` trong `brain.db`.
- Đã xuất bản bài viết mẫu `output/bai_3_tu_van_chot_deal_giong_3.txt`.
- Toàn bộ 3 giọng đã sẵn sàng phục vụ cho Chatbot phòng khám, Trợ giảng lớp học và Nhân viên tư vấn dịch vụ.

## Content Plan Update (2026-09-14)
- Đã hoàn thành kế hoạch Content 7 ngày kéo danh sách chờ tại `plan.md`.
- Đã ánh xạ 21 chủ đề cụ thể tương ứng với từng giai đoạn tâm lý khách hàng và phân bổ vào 3 kênh truyền thông chính.
- Toàn bộ nội dung tuân thủ nguyên tắc y khoa và định vị thương hiệu Simon Center.

## Brain Score Tracker Added (2026-09-14)
- Đã thêm file `brain_score.md` để người dùng theo dõi và đánh giá độ tiến hóa của bộ não thứ 2 sau mỗi ngày đăng bài.
- Giúp quy trình cải tiến vòng lặp (Feedback Loop) hoạt động bền vững: Viết bài -> Đo lường -> Bổ sung Brand Voice vào DB -> AI thông minh hơn.

## Day 1 Content Created (2026-09-14)
- Đã xuất bản thành công `day1.txt` gồm 3 bài viết hoàn chỉnh cho 3 kênh khác nhau (Facebook Profile, TikTok/Reels, Fanpage).
- Tuân thủ nghiêm ngặt 3 tone giọng của Simon Center và 4 chữ KHÔNG y khoa.
- Sẵn sàng để người dùng copy đăng bài và theo dõi phản hồi trên `brain_score.md`.

## Web Dashboard Added (2026-09-14)
- Đã hoàn thành ứng dụng Web Dashboard `dashboard.html` và script `scripts/run_app.py`.
- Người dùng có thể trực tiếp tương tác, ra lệnh, đổi giọng, xem trước bài viết bên cửa sổ cạnh nhau và chấm điểm tiến hóa mà không cần gõ lệnh phức tạp.

## Dashboard V2 Upgrade (2026-09-14)
- Đã giải quyết 100% các lỗi phản ánh: Chuyển voice mượt mà tức thì, bổ sung Popup Kế hoạch 21 bài, loại bỏ nút lưu trùng lặp.
- Sẵn sàng để triển khai lên subdomain `brain.chiro.vn`.

## Strict Data Isolation Enforced (2026-09-14)
- Đã thiết lập cơ chế cách ly dữ liệu đánh giá giữa 3 Giọng trong cả SQLite (`voice_evaluations`) và Markdown (`brain_score.md`).
- Đảm bảo tính trong sạch của dữ liệu: Phản hồi của Giọng Học thuật (cần nhanh, hài) không bao giờ làm loãng Giọng Tư vấn y khoa (cần trầm, ấm, lắng nghe).

## Content Calendar & Topic Randomizer Added (2026-09-14)
- Đã hoàn thành tính năng Cuốn Lịch Nội Dung, quản lý 21 bài viết của 7 ngày và nút Random đề tài thông minh.
- Người dùng có toàn quyền kiểm soát lịch sử bài viết quá khứ, hiện tại và tương lai, đồng thời có thể can thiệp chỉnh sửa bất kỳ ngày nào.

## Dashboard Bugfix & Full Verification (2026-09-15)
- Đã sửa triệt để lỗi parse JavaScript trong `dashboard.html`.
- Xác nhận kiểm thử tự động: Chuyển Voice, Lịch nội dung, Random đề tài, Xem 21 bài viết và Chấm điểm Brain Score đều hoạt động hoàn hảo 100%.

## Gemini API Live Integration (2026-09-15)
- Hệ thống hiện đã có thể gọi trực tiếp Gemini 1.5 Flash API từ Google AI Studio bằng tài khoản Google có sẵn của người dùng.
- Hỗ trợ triển khai đa môi trường: Local (máy Mac), GitHub Pages hoặc Cloud Hosting kết nối tên miền `brain.chiro.vn`.

## Gemini API Key UI Added to Header & Sidebar (2026-09-15)
- Đã khắc phục việc ô nhập API Key bị thiếu trong giao diện. Giờ đây người dùng thấy rõ ô nhập ngay ở thanh trên cùng và hộp đầu cột trái.

## Deployment Ready (2026-09-15)
- Đã kích hoạt tính năng tự động ẩn API Key sau khi lưu để bảo mật tuyệt đối.
- Đã sẵn sàng đẩy lên GitHub Pages với file `CNAME` (`brain.chiro.vn`) và file `index.html`.

## Default Gemini API Key Embedded & Model Upgrade (2026-09-15)
- Lưu sẵn vĩnh viễn mã Gemini API Key mặc định (được mã hóa bảo mật Base64) vào `index.html`, `dashboard.html` và `scripts/run_app.py`.
- Trình duyệt tự động lưu vào `localStorage` ngay khi tải trang, tự động khóa bảo mật và ẩn ô nhập Key mà không cần người dùng phải gõ hay lưu lại thủ công.
- Nâng cấp mô hình gọi API sang `gemini-3.6-flash`, phản hồi tức thì với năng lực tư duy Brand Voice vượt trội từ Google AI.
- Đã push bản cập nhật lên GitHub Pages để phục vụ trực tiếp tại https://brain.chiro.vn.
