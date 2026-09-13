# My Brain - Second Brain System

Hệ thống Bộ Não Thứ 2 (Second Brain) cá nhân hoá, lưu trữ kiến thức, dữ liệu kinh doanh và định vị Brand Voice.
Hệ thống được thiết kế để tích hợp liền mạch với các AI Coding Agents (Google Antigravity, Claude Code, Cursor) thông qua cơ chế tài liệu tự động và bộ nhớ Handoff.

## Cấu trúc thư mục

```
my-brain/
├── README.md           # Giới thiệu tổng quan & hướng dẫn sử dụng
├── ARCHITECTURE.md     # Thiết kế kiến trúc và mô hình dữ liệu
├── CHANGELOG.md        # Lịch sử các thay đổi của project
├── TODO.md             # Danh sách công việc cần làm tiếp theo
├── HANDOFF.md          # Sổ bàn giao trạng thái giữa các AI Agent
├── .gitignore          # Cấu hình bỏ qua các file không cần commit
├── brain.db            # Cơ sở dữ liệu SQLite cục bộ
├── scripts/            # Các scripts tiện ích và khởi tạo
│   └── create_db.py    # Script khởi tạo/cập nhật database
└── output/             # Thư mục chứa các bài viết do AI sinh ra
    └── post.txt        # Bài viết xuất bản mẫu
```

## Bắt đầu nhanh

1. Khởi tạo database:
   ```bash
   python3 scripts/create_db.py
   ```
2. Cập nhật dữ liệu Brand Voice cá nhân vào `brain.db`.
3. Nhờ AI Agent đọc `brain.db` và sinh bài viết mới.
