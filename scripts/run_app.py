import os
import sys
import json
import sqlite3
import urllib.request
import urllib.error
import http.server
import socketserver
import webbrowser

PORT = 8080
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(base_dir)
db_path = os.path.join(base_dir, 'brain.db')

# Helper: Call Google Gemini API
def call_gemini_api(api_key, model_name, prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 2048
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers)
    
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        try:
            return res_data['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError):
            return "Không thể nhận diện nội dung từ Google Gemini API."

class SecondBrainAPIHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/generate':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            req_json = json.loads(post_data.decode('utf-8'))

            api_key = req_json.get('api_key') or os.environ.get('GEMINI_API_KEY')
            voice_key = req_json.get('voice', 'voice1')
            topic = req_json.get('topic', 'Chăm sóc sức khỏe cột sống')
            channel = req_json.get('channel', 'Facebook Cá Nhân')
            custom_prompt = req_json.get('custom_prompt', '')

            if not api_key:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Vui lòng cung cấp Gemini API Key."}).encode('utf-8'))
                return

            # Read system prompt & brand voice from brain.db
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.execute("SELECT title, content FROM brand_voice")
            brand_records = cur.fetchall()
            conn.close()

            brand_context = "\n\n".join([f"=== {r[0]} ===\n{r[1]}" for r in brand_records])

            full_prompt = f"""Bạn là trợ lý mang tiếng nói của người sáng lập Simon Center (Chiropractic & Phục hồi chức năng tại TP.HCM).
Dưới đây là tri thức, nguyên tắc y khoa và định vị Brand Voice độc quyền từ database brain.db của Simon Center:

{brand_context}

---
YÊU CẦU BÀI VIẾT:
- Chủ đề: "{topic}"
- Kênh đăng: {channel}
- Tone giọng yêu cầu: {voice_key.upper()} (Hãy tuân thủ đúng định vị của giọng này từ database trên).
- Gợi ý bổ sung từ người dùng: {custom_prompt if custom_prompt else "Không có"}

HÃY VIẾT MỘT BÀI ĐĂNG HOÀN CHỈNH:
1. Bắt đầu bằng hook thu hút.
2. Tuân thủ nghiêm ngặt 4 chữ KHÔNG y khoa (không chẩn đoán online, không bán thuốc, không trấn an bừa bãi, không hù dọa).
3. Câu cú chuẩn xác theo văn hóa Việt Nam (xưng hô ấm áp: anh/chị - em, dạ đầu câu, dùng 'nhé ạ').
4. Có lời kêu gọi hành động (CTA) khéo léo dẫn dắt người đọc đăng ký vào Form Danh Sách Chờ (Waitlist) Buổi Đánh Giá Cột Sống 1-1 chuyên sâu tại Simon Center.
5. Kết thúc bài viết bằng câu lưu ý tham khảo y khoa bắt buộc."""

            try:
                ai_result = call_gemini_api(api_key, "gemini-1.5-flash", full_prompt)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"content": ai_result}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

        elif self.path == '/api/evaluate':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            req_json = json.loads(post_data.decode('utf-8'))

            day_number = req_json.get('day', 1)
            voice_key = req_json.get('voice_key', 'voice1')
            voice_name = req_json.get('voice_name', 'Giọng 1')
            channel = req_json.get('channel', '')
            topic = req_json.get('topic', '')
            score = req_json.get('score', 9.0)
            feedback = req_json.get('feedback', '')
            rules = req_json.get('rules', '')
            notes = req_json.get('notes', '')

            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.execute('''
                INSERT INTO voice_evaluations 
                (day_number, voice_key, voice_name, channel, topic, score, audience_feedback, voice_rules_added, review_notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (day_number, voice_key, voice_name, channel, topic, score, feedback, rules, notes))
            conn.commit()
            conn.close()

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "message": "Đã lưu đánh giá vào SQLite brain.db!"}).encode('utf-8'))

        else:
            super().do_POST()

def main():
    url = f"http://localhost:{PORT}/dashboard.html"
    print("=" * 70)
    print("🚀 SIMON CENTER SECOND BRAIN WEB SERVER + GEMINI API ĐANG CHẠY...")
    print(f"📍 Mở trình duyệt tại: {url}")
    print("=" * 70)

    try:
        with socketserver.TCPServer(("", PORT), SecondBrainAPIHandler) as httpd:
            print(f"Server đang lắng nghe tại port {PORT}... (Bấm Ctrl+C để dừng)")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng server.")
    except Exception as e:
        print(f"Lỗi khởi động server: {e}")

if __name__ == '__main__':
    main()
