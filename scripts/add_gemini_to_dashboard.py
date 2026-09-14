with open('/Users/huybui/Desktop/my-brain/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add API Key Bar to the Header
header_action_old = '<span class="text-xs text-slate-400 font-mono hidden md:inline">domain: brain.chiro.vn</span>'
header_action_new = '''<div class="flex items-center gap-1.5">
        <input type="password" id="geminiApiKeyInput" placeholder="Dán Gemini API Key vào đây..." class="bg-slate-100 border border-slate-200 rounded-xl px-3 py-1.5 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 w-48 font-mono">
        <button onclick="saveApiKey()" class="px-2.5 py-1.5 bg-blue-600 hover:bg-blue-700 text-white rounded-xl text-xs font-bold transition flex items-center gap-1" title="Lưu khóa API">
          <i class="fa-solid fa-key text-[10px]"></i> Lưu Key
        </button>
      </div>'''

content = content.replace(header_action_old, header_action_new)

# 2. Update generateLiveArticle in JavaScript to call Gemini API if key is present
old_generate = """    // 8. GENERATE LIVE ARTICLE
    function generateLiveArticle() {
      const topic = document.getElementById('topicInput').value;
      const customPrompt = document.getElementById('customPromptInput').value;
      document.getElementById('displayTopicTitle').textContent = `Chủ đề: "${topic}"`;"""

new_generate = """    // 8. GENERATE LIVE ARTICLE (WITH REAL GEMINI API)
    async function generateLiveArticle() {
      const topic = document.getElementById('topicInput').value;
      const customPrompt = document.getElementById('customPromptInput').value;
      const channel = document.getElementById('channelSelect').selectedOptions[0].text;
      document.getElementById('displayTopicTitle').textContent = `Chủ đề: "${topic}"`;

      const apiKey = localStorage.getItem('simon_gemini_api_key') || document.getElementById('geminiApiKeyInput').value.trim();

      // If user provided an API key, call real Gemini AI!
      if (apiKey) {
        showToast('Đang gọi Google Gemini 1.5 Flash tạo bài viết thật...');
        document.getElementById('postTextContent').textContent = 'Đang suy luận theo Brand Voice của Simon Center từ database...';
        
        try {
          // Direct call to Gemini 1.5 Flash endpoint
          const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              contents: [{
                parts: [{
                  text: `Bạn là trợ lý mang tiếng nói của người sáng lập Simon Center (Chiropractic & PHCN tại TP.HCM).
Dưới đây là tri thức Brand Voice từ database brain.db:
- Giọng 1: Thấu cảm, ấm áp, lắng nghe nỗi đau bệnh nhân (Gabor Maté + BS Trần Văn Phúc).
- Giọng 2: Giảng học thuật sinh động, First Principles, đập tan myth bằng khoa học, hóm hỉnh (Doctor Mike + Elon Musk).
- Giọng 3: Sale y đức, Feel-Felt-Found, sức khỏe trước doanh số, chốt lịch đánh giá (Francis Hùng).
- Bốn chữ KHÔNG y khoa: Không chẩn đoán online, không bán thuốc, không trấn an bừa, không hù dọa.
- Xưng hô: anh/chị - em, dạ đầu câu, dùng 'nhé ạ'.

YÊU CẦU BÀI VIẾT:
- Chủ đề: "${topic}"
- Kênh: ${channel}
- Tone giọng yêu cầu: ${currentVoice.toUpperCase()}
- Lưu ý riêng của bạn: ${customPrompt ? customPrompt : "Không có"}

HÃY VIẾT 1 BÀI ĐĂNG HOÀN CHỈNH: Có hook thu hút, nội dung sâu sắc, đúng tone, CTA kéo vào form danh sách chờ (Waitlist) buổi đánh giá cột sống 1-1, và câu miễn trừ y khoa cuối bài.`
                }]
              }],
              generationConfig: { temperature: 0.7, maxOutputTokens: 2048 }
            })
          });
          
          const json = await res.json();
          if (json.candidates && json.candidates[0].content.parts[0].text) {
            const aiText = json.candidates[0].content.parts[0].text;
            document.getElementById('postTextContent').textContent = aiText;
            const words = aiText.trim().split(/\\s+/).length;
            document.getElementById('charCount').innerHTML = `<i class="fa-solid fa-align-left mr-1"></i> ${words} từ • ~${Math.ceil(words/180)} phút đọc`;
            showToast('Google Gemini đã sinh bài viết thật 100%!');
            return;
          }
        } catch (err) {
          console.warn('API error, falling back to local pre-trained generator', err);
        }
      }"""

content = content.replace(old_generate, new_generate)

# 3. Add saveApiKey helper
save_api_helper = """    function saveApiKey() {
      const k = document.getElementById('geminiApiKeyInput').value.trim();
      if (!k) {
        alert('Vui lòng dán mã Gemini API Key.');
        return;
      }
      localStorage.setItem('simon_gemini_api_key', k);
      showToast('Đã lưu Gemini API Key! Giờ bạn có thể sinh bài thật 100%!');
    }

    function checkSavedApiKey() {
      const saved = localStorage.getItem('simon_gemini_api_key');
      if (saved) {
        document.getElementById('geminiApiKeyInput').value = saved;
      }
    }
"""

content = content.replace("    // 9. RENDER ALL 7 DAYS IN MODAL", save_api_helper + "\n    // 9. RENDER ALL 7 DAYS IN MODAL")
content = content.replace("inspectDay(1);", "inspectDay(1);\n      checkSavedApiKey();")

with open('/Users/huybui/Desktop/my-brain/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Gemini API directly embedded into dashboard.html!")
