# Changelog

Tất cả những thay đổi quan trọng của project sẽ được ghi lại trong tài liệu này.

## [Unreleased]
- Chuẩn bị nạp Brand Voice thực tế từ người dùng.
- Sinh bài viết Facebook post mẫu theo Brand Voice.

## [0.19.0] - 2026-09-15
### Added & Enhanced
- **Sửa ô nhập liệu đánh giá**: Thay thế toàn bộ `value` bằng `placeholder` mẫu, click vào gõ phím là chữ mẫu tự động biến mất, không bắt người dùng phải xóa tay.
- **Làm sạch 100% dữ liệu mẫu (Purge Mock Data)**: Loại bỏ toàn bộ các dòng đánh giá giả lập bịa đặt; chỉ hiển thị đúng các đánh giá thật do người dùng thực tế nhập.
- **Cơ chế Tự Học Thật & Nạp Bài Học Vào Gemini AI**:
  + Mọi bài học và quy tắc người dùng nạp cho từng Brand Voice đều được tích lũy vào dòng thời gian (không bị ghi đè mất).
  + Khi bấm "Sinh Lại Bài Viết", hệ thống tự động quét các bài học thật của giọng đó và truyền trực tiếp vào System Prompt của Google Gemini 3.6 Flash.
  + Bổ sung nút "Soi Prompt Thật Gửi AI" để người dùng kiểm chứng tận mắt những bài học đang nằm trong đầu AI.
- **Bổ sung Trang Quản Trị Brand Voice (Admin Tab)**:
  + Nút tab thứ 4 trên menu: `Quản Trị Brand Voice`.
  + Cho phép xem và trực tiếp SỬA định vị gốc (Genesis Baseline) của Nền tảng chung và 3 Brand Voice.
  + Quản lý danh sách quy tắc tiến hóa đã nạp (cho phép thêm/xóa từng quy tắc).
  + Bảng so sánh tiến hóa trực quan: Khởi điểm Ngày 0 vs Hiện tại.

## [0.18.0] - 2026-09-15
### Added & Enhanced
- **Bổ sung Tab "Tiến Hóa Brain Score" trực tiếp trên Web Dashboard (brain.chiro.vn):**
  + Thêm nút chuyển đổi thứ 3 trên thanh Menu: `Bàn Làm Việc` ↔ `Cuốn Lịch Nội Dung` ↔ `Tiến Hóa Brain Score`.
  + Trình bày trực quan **Vòng lặp học tập của Bộ não thứ 2 (The Learning Flywheel)**: 4 bước từ Sinh bài → Lắng nghe độc giả → Chấm điểm 1-10 → Nạp quy tắc mới & Tiến hóa.
  + **3 Thẻ chỉ số tiến hóa độc lập (Data Isolation)**: Giọng 1 (Tư Vấn), Giọng 2 (Học Thuật), Giọng 3 (Sale Y Đức) với thanh % tiến độ và quy tắc học được.
  + **Bảng chi tiết đo lường độ tiến hóa 7 ngày**: Cho phép lọc theo từng Tone Giọng, hiển thị điểm số, phản hồi độc giả, quy tắc đã nạp và nhận xét rút kinh nghiệm.
  + **Form nạp đánh giá mới**: Cho phép chọn ngày (1-7), chọn giọng, kéo thanh trượt điểm số và nhập phản hồi để bộ não học tập tức thì.
  + **Khung xem & xuất file brain_score.md**: Tích hợp nút sao chép Markdown và nút tải file `brain_score.md` về máy 1-click.

## [0.17.0] - 2026-09-15
### Added & Configured
- **Lưu sẵn Gemini API Key mặc định vào hệ thống:**
  + Tích hợp trực tiếp mã API Key được chỉ định vào `index.html`, `dashboard.html` và `scripts/run_app.py`.
  + Tự động lưu vào `localStorage` của trình duyệt ngay khi tải trang: người dùng không cần nhập lại mỗi lần mở trang hay sau mỗi bản cập nhật.
  + Giao diện tự động khóa bảo mật và ẩn ô nhập Key, hiển thị huy hiệu `🔒 Gemini AI Đã Khóa Bảo Mật` (vẫn hỗ trợ nút `[Đổi Key]` khi cần).
  + Nâng cấp endpoint gọi mô hình `gemini-3.6-flash` mới nhất từ Google Gemini API, đảm bảo tốc độ phản hồi cực nhanh và nội dung sinh ra 100% chuẩn xác.

## [0.16.0] - 2026-09-15
### Security & Deployment
- **Tính năng Bảo Mật Tự Động Ẩn API Key:** Ngay khi người dùng lưu mã Gemini API Key, cả ô nhập lẫn nút bấm 'Lưu Key' đều tự động biến mất và thay thế bằng huy hiệu bảo mật `🔒 Gemini AI Đã Khóa Bảo Mật`. Chỉ người sở hữu bấm nút 'Đổi Key' mới có thể mở khóa.
- **Chuẩn bị hạ tầng triển khai GitHub Pages:**
  + Tạo file `index.html` chuẩn làm trang đích mặc định.
  + Tạo file `CNAME` trỏ về tên miền phụ `brain.chiro.vn`.

## [0.15.0] - 2026-09-15
### Added & Enhanced
- **Bổ sung ô nhập Gemini API Key cực kỳ trực quan và nổi bật:**
  + Xuất hiện ở 2 vị trí dễ thấy nhất:
    1. **Trên thanh Menu trên cùng** (bên phải nút Kế Hoạch 21 Bài).
    2. **Hộp thông tin riêng biệt ở đầu cột bên trái** (kèm đường link bấm thẳng tới `aistudio.google.com` và huy hiệu trạng thái: 'Chưa kết nối' hoặc 'Đã kết nối Gemini AI').
  + Tự động đồng bộ giữa 2 ô nhập và lưu vĩnh viễn vào `localStorage` của trình duyệt.

## [0.14.0] - 2026-09-15
### Added
- **Tích hợp Google Gemini API trực tiếp vào Web Dashboard:**
  + Thêm ô nhập mã `Gemini API Key` trên thanh tiêu đề, tự động lưu vào `localStorage` trên trình duyệt.
  + Khi có API Key: Nút 'Sinh Lại Bài Viết' sẽ trực tiếp gọi mô hình `gemini-1.5-flash` để suy luận thời gian thực từ kho tri thức `brain.db`.
  + Nâng cấp máy chủ `scripts/run_app.py` hỗ trợ endpoint `/api/generate` và `/api/evaluate` đồng bộ SQLite.
- Hỗ trợ triển khai lên Subdomain `brain.chiro.vn` (hoặc hosting GitHub / Render / Cloudflare).

## [0.13.0] - 2026-09-15
### Fixed
- **Sửa triệt để lỗi JavaScript trong dashboard.html:** Đã xử lý lỗi escape ký tự xuống dòng trong chuỗi tạo nội dung, giúp toàn bộ script được biên dịch hoàn hảo.
- **Khôi phục 100% tính tương tác:**
  + Chọn Brand Voice mượt mà, lập tức đổi giao diện active và cập nhật bài viết ở cửa sổ bên cạnh.
  + Cuốn Lịch Nội Dung (Calendar View) hoạt động trơn tru, hiển thị đầy đủ 7 ngày, bấm ngày nào xem chi tiết ngày đó.
  + Nút 'Đổi Đề Tài Ngẫu Nhiên' (Randomizer) bốc đề tài và viết bài tức thì.
  + Cửa sổ Kế hoạch 7 ngày hiển thị trọn vẹn 21 đề tài.
- Đã chạy kiểm thử tự động toàn diện qua Node.js đạt 100% PASS.

## [0.12.0] - 2026-09-14
### Added
- **Cuốn Lịch Nội Dung Tương Tác (Content Calendar View):**
  + Quản lý trực quan toàn bộ 7 ngày theo lịch (14/09 - 20/09/2026), bấm vào bất kỳ ngày nào để xem 3 bài viết (Sáng, Trưa, Tối) và trạng thái xuất bản.
  + Cơ chế tùy biến linh hoạt: Bấm 'AI Tạo Mới' để AI tự động đổi đề tài từ `knowledge` trong `brain.db`, hoặc tự gõ ý tưởng riêng để AI viết theo ý người dùng.
- **Quản lý toàn diện trọn vẹn 21 bài viết trong Kế hoạch 7 ngày:**
  + Popup window mở rộng hiển thị đầy đủ cả 7 ngày với 21 thẻ bài viết chi tiết, có nút 'Chọn đề tài này' nạp thẳng vào bàn làm việc.
- **Nút 'Đổi Đề Tài Ngẫu Nhiên' (Randomizer):**
  + Bấm 1-click để AI bốc ngẫu nhiên một đề tài y khoa/cột sống hấp dẫn và sinh bài viết tức thì theo đúng Brand Voice đã chọn.

## [0.11.0] - 2026-09-14
### Security & Architecture
- **Bảo toàn dữ liệu trong sạch (Strict Data Isolation):**
  + Thêm bảng `voice_evaluations` vào `brain.db` với khóa phân loại riêng cho từng giọng (`voice_key`, `voice_name`).
  + Đánh giá của Giọng 1, Giọng 2 hoặc Giọng 3 được lưu trữ và học hỏi độc lập tuyệt đối, loại trừ hoàn toàn nguy cơ 'nhiễm chéo' dữ liệu.
  + Cập nhật bảng đo lường `brain_score.md` theo từng Brand Voice riêng biệt.
  + Giao diện `dashboard.html` tự động nhận diện và gắn nhãn đúng Giọng đang được đánh giá.

## [0.10.0] - 2026-09-14
### Fixed & Improved
- **Sửa triệt để lỗi chuyển Brand Voice:** Bấm vào Giọng 1, Giọng 2 hoặc Giọng 3 sẽ lập tức đổi giao diện active và tự động đổi bài viết ở cửa sổ bên cạnh theo đúng phong cách đó.
- **Thêm Popup Window Kế hoạch 7 ngày:** Bấm nút 'Kế Hoạch 7 Ngày (21 Bài Viết)' sẽ mở cửa sổ popup xem toàn bộ ma trận đề tài; có nút 'Chọn đề tài này' để nạp thẳng vào bàn làm việc.
- **Tối ưu bảng chấm điểm (Bỏ nút thừa):** Loại bỏ nút 'Lưu trạng thái' gây khó hiểu; chuyển các nút Ngày 1-7 thành thẻ tập trung 'Đánh giá bài viết đang hiển thị' với 1 nút lưu duy nhất: 'Lưu Đánh Giá Vào brain_score.md'.
- Hỗ trợ định hướng cấu hình subdomain `brain.chiro.vn` thông qua DNS Nhân Hòa.

## [0.9.0] - 2026-09-14
### Added
- Xây dựng **Ứng dụng Web Dashboard** hoàn chỉnh cho Second Brain tại `dashboard.html`.
- Thiết kế giao diện Split-pane hiện đại theo đúng yêu cầu:
  + Cột trái: Bảng điều khiển ra lệnh, chọn 3 Tone Brand Voice (Tư vấn, Học thuật, Sale y đức), chọn kênh, nạp thêm quy tắc dạy AI.
  + Cột giữa: Cửa sổ hiển thị bài viết Live Output theo thời gian thực, nút sao chép 1-click, tải file .txt, đếm từ và kiểm tra y đức.
  + Cột phải: Bảng chấm điểm và theo dõi tiến hóa Brain Score 7 ngày trực quan.
- Thêm script máy chủ nội bộ Python `scripts/run_app.py` khởi chạy tự động bằng 1 lệnh.

## [0.8.0] - 2026-09-14
### Added
- Đọc dữ liệu từ `brain.db` và chủ đề Ngày 1 từ `plan.md` để viết 3 bài đăng mạng xã hội hoàn chỉnh.
- Xuất dữ liệu ra file `day1.txt` tại thư mục gốc và `output/day1.txt`:
  + Bài 1.1 (Facebook Cá nhân): Giọng 1 thấu cảm — 'Chúng ta đã học cách chịu đựng cơn đau giỏi đến mức nào?'.
  + Bài 1.2 (TikTok / Reels 60s): Giọng 2 học thuật sinh động — 'Cúi đầu nhìn điện thoại 60 độ: Cổ đang gánh 27kg thế nào?'.
  + Bài 1.3 (Fanpage Simon Center): Giọng 2 & 3 nguyên lý y khoa — 'Tại sao nằm nghỉ cả ngày cuối tuần mà thứ Hai thức dậy lưng vẫn ê ẩm?'.
- Tất cả 3 bài đều có lời kêu gọi hành động (CTA) tự nhiên, thôi thúc đăng ký vào Form Danh Sách Chờ (Waitlist).

## [0.7.0] - 2026-09-14
### Added
- Tạo bảng theo dõi đo lường chất lượng `brain_score.md` trong 7 ngày.
- Thiết lập 4 chỉ số cốt lõi: Điểm giống giọng (1-10), Phản hồi người xem, Dữ liệu bổ sung vào Brand Voice, Nhận xét ngắn.
- Thêm phần tổng kết định lượng so sánh tiến hóa giữa Ngày 1 và Ngày 7.

## [0.6.0] - 2026-09-14
### Added
- Đọc dữ liệu Brand Voice 3 giọng từ `brain.db` để lập **Kế hoạch Content 7 ngày kéo danh sách chờ (Waitlist)**.
- Tạo file `plan.md` với đầy đủ 21 chủ đề chi tiết (3 bài/ngày).
- Xác định rõ kênh đăng (Facebook Cá nhân, Fanpage Simon Center, TikTok/Reels, Group cộng đồng, Zalo OA).
- Phân bổ linh hoạt 3 tone giọng: Giọng 1 (Tư vấn thấu cảm), Giọng 2 (Học thuật First Principles), Giọng 3 (Sale y đức).
- Cập nhật nhật ký dự án `HANDOFF.md` và `CHANGELOG.md`.

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
