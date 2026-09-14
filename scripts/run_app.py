import os
import sys
import webbrowser
import http.server
import socketserver

PORT = 8080
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(base_dir)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    url = f"http://localhost:{PORT}/dashboard.html"
    print("=" * 60)
    print("🚀 SIMON CENTER SECOND BRAIN WEB DASHBOARD ĐANG CHẠY...")
    print(f"📍 Mở trình duyệt tại: {url}")
    print("=" * 60)
    
    # Try opening browser automatically
    try:
        webbrowser.open(url)
    except Exception:
        pass

    try:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print(f"Server đang lắng nghe tại port {PORT}... (Bấm Ctrl+C để dừng)")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng server.")
    except Exception as e:
        print(f"Lỗi: {e}")
        # If port is busy or anything, open file directly
        direct_file = os.path.join(base_dir, 'dashboard.html')
        print(f"Bạn có thể mở trực tiếp file tại: {direct_file}")
        webbrowser.open(f"file://{direct_file}")

if __name__ == '__main__':
    main()
