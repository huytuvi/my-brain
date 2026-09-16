# HƯỚNG DẪN BẢO VỆ TRI THỨC NÃO BỘ (DATA PERSISTENCE & MIGRATION)
## Làm sao để thường xuyên cập nhật phiên bản mới cho phần mềm mà không bị ghi đè dữ liệu brain.db?

---

### 1. NGUYÊN NHÂN GỐC RỄ VÌ SAO DỮ LIỆU CÓ THỂ BỊ GHI ĐÈ KHI CẬP NHẬT
Trong các dự án phần mềm trí tuệ nhân tạo (Second Brain), có 2 thành phần hoàn toàn khác nhau:
1. **Mã nguồn (Codebase)**: Các file `.html`, `.js`, `.py`, các thuật toán prompt, layout giao diện. Đây là phần **thường xuyên được cập nhật phiên bản mới**.
2. **Trạng thái tri thức (Brain State / Data)**: Các bài học SOP, điểm số, Blacklist từ cấm, Case study lâm sàng, các đoạn văn mẫu mà chính bạn đã dày công dạy cho AI.

**Nguy cơ xảy ra khi**: File lưu trữ dữ liệu (như `brain.db` hoặc dữ liệu mẫu trong code) bị đưa chung vào Git và quản lý như file code tĩnh. Mỗi lần lập trình viên hoặc lệnh `git pull` / deploy version mới diễn ra, Git có thể ghi đè file database mẫu lên trên database thật đang chứa dữ liệu của bạn.

---

### 2. GIẢI PHÁP 4 TẦNG ĐÃ ĐƯỢC TRIỂN KHAI HOÀN CHỈNH

#### Tầng 1: Bộ Công Cụ "Sao Lưu & Khôi Phục Não Bộ 1-Click" (Ngay Trên Web Dashboard)
- **Vị trí**: Nằm ở tab **Tiến Hóa Brain Score** (cạnh nút Tải về .md) và tab **Quản Trị Brand Voice (Admin - Tab 6)** trên [brain.chiro.vn](https://brain.chiro.vn).
- **Cách dùng**:
  - **Sao Lưu (Export JSON)**: Bấm nút **"Sao Lưu Não Bộ (JSON)"**, hệ thống đóng gói 100% dữ liệu đã thu thập (Đánh giá SOP, Điểm số, Blacklist, Case study, Luật ngầm, Văn mẫu và Cấu hình 3 Giọng) thành file `brain_backup_YYYY-MM-DD.json` lưu về máy tính bạn.
  - **Khôi Phục (Import JSON)**: Khi phần mềm cập nhật version lớn, hoặc khi bạn đổi máy tính/trình duyệt, chỉ cần bấm **"Khôi Phục Não Bộ (JSON)"** và chọn file backup. Hệ thống sẽ **tự động hợp nhất thông minh (Smart Merge)**:
    + Giữ nguyên các dữ liệu hiện có.
    + Nạp thêm các bài học chưa có.
    + Không bao giờ xóa hay đè mất dữ liệu.

#### Tầng 2: Công Cụ Đồng Bộ An Toàn Hai Chiều `scripts/sync_brain.py` (Cho SQLite brain.db)
Để file cơ sở dữ liệu `brain.db` trên máy tính/máy chủ của bạn luôn được cập nhật mà không bị mất mát:
1. **Nạp dữ liệu từ file backup JSON vào SQLite `brain.db`**:
   ```bash
   python3 scripts/sync_brain.py --import brain_backup_2026-09-16.json
   ```
   *Lệnh này sử dụng cơ chế `Idempotent Insert` (kiểm tra trùng lặp trước khi nạp), đảm bảo không ghi đè, không nhân bản dữ liệu rác.*
2. **Trích xuất dữ liệu từ SQLite `brain.db` ra file JSON**:
   ```bash
   python3 scripts/sync_brain.py --export
   ```

#### Tầng 3: Khóa File `brain.db` Khỏi Sự Can Thiệp Của Git (Git Ignore / Assume Unchanged)
Để mỗi lần lập trình viên `git pull` cập nhật code mới mà Git không bao giờ chạm vào file `brain.db` trên máy bạn:
Chạy lệnh sau trong terminal:
```bash
git update-index --assume-unchanged brain.db
```
*Lệnh này báo cho Git: "Hãy bỏ qua mọi thay đổi của file brain.db, không bao giờ kéo đè file này khi cập nhật code".*

#### Tầng 4: Giải Pháp Đám Mây Vĩnh Viễn (Cloud Database - Supabase / Firebase / Cloudflare D1)
Nếu bạn muốn bất kỳ ai trong nhóm hoặc bạn dù mở máy tính ở công ty, laptop ở nhà hay điện thoại di động đều truy cập chung một bộ não duy nhất:
- Chúng ta có thể kết nối backend của bạn tới một **Cloud Database miễn phí (Supabase PostgreSQL hoặc Firebase Firestore)**.
- Khi đó:
  + Frontend `brain.chiro.vn` có thể update 100 phiên bản mỗi ngày mà không ảnh hưởng tới Database.
  + Database nằm độc lập 100% trên Cloud, liên tục tích lũy và học hỏi 24/7.

---

### 3. TÓM TẮT QUY TRÌNH VẬN HÀNH AN TOÀN CHO BẠN
1. Hàng tuần hoặc sau khi nạp nhiều bài học SOP hay, bạn chỉ cần bấm **"Sao Lưu Não Bộ (JSON)"** để lưu 1 bản dự phòng về máy.
2. Cứ thoải mái yêu cầu nâng cấp, thêm tính năng mới cho phần mềm `brain.chiro.vn`.
3. Toàn bộ code mới được viết theo nguyên tắc **Non-destructive Initialization** (chỉ bổ sung tính năng mới, không xóa hay ghi đè bộ nhớ tri thức đã có).
