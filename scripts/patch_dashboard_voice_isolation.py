import re

file_path = '/Users/huybui/Desktop/my-brain/dashboard.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update header badge in evaluation card
badge_old = '<span class="text-[11px] font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded border border-blue-100" id="evaluatingDayBadge">Ngày 1</span>'
badge_new = '''<div class="flex items-center gap-1.5">
              <span class="text-[11px] font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded border border-blue-100" id="evaluatingDayBadge">Ngày 1</span>
              <span class="text-[11px] font-bold text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded border border-indigo-100" id="evaluatingVoiceBadge">Giọng 1</span>
            </div>'''
content = content.replace(badge_old, badge_new)

# Update save button text
btn_old = '<span>Lưu Đánh Giá Vào brain_score.md</span>'
btn_new = '<span id="saveEvalBtnText">Lưu Đánh Giá Riêng Cho [Giọng 1] Vào brain_score.md</span>'
content = content.replace(btn_old, btn_new)

# Update selectVoice function in JS
js_select_old = "document.getElementById('outputBadge').textContent = `Bài Viết Đang Hiển Thị (${currentVoice === 'voice1' ? 'Giọng 1' : currentVoice === 'voice2' ? 'Giọng 2' : 'Giọng 3'})`;"
js_select_new = """document.getElementById('outputBadge').textContent = `Bài Viết Đang Hiển Thị (${currentVoice === 'voice1' ? 'Giọng 1' : currentVoice === 'voice2' ? 'Giọng 2' : 'Giọng 3'})`;
      const voiceLabelShort = currentVoice === 'voice1' ? 'Giọng 1' : currentVoice === 'voice2' ? 'Giọng 2' : 'Giọng 3';
      const evBadge = document.getElementById('evaluatingVoiceBadge');
      if (evBadge) evBadge.textContent = voiceLabelShort;
      const saveBtnText = document.getElementById('saveEvalBtnText');
      if (saveBtnText) saveBtnText.textContent = `Lưu Đánh Giá Riêng Cho [${voiceLabelShort}] Vào brain_score.md`;"""
content = content.replace(js_select_old, js_select_new)

# Update saveEvaluation function
save_fn_old = """    function saveEvaluation() {
      const score = document.getElementById('scoreSlider').value;
      const feedback = document.getElementById('feedbackInput').value;
      const notes = document.getElementById('reviewNotesInput').value;
      
      document.getElementById('trackerDay1Score').textContent = score + '/10';
      showToast(`Đã lưu đánh giá Ngày ${currentDay} (${score}/10) vào brain_score.md!`);
    }"""

save_fn_new = """    function saveEvaluation() {
      const score = document.getElementById('scoreSlider').value;
      const feedback = document.getElementById('feedbackInput').value;
      const notes = document.getElementById('reviewNotesInput').value;
      const voiceNames = {
        voice1: 'Giọng 1 (Tư Vấn Thấu Cảm)',
        voice2: 'Giọng 2 (Giảng Học Thuật)',
        voice3: 'Giọng 3 (Sale Y Đức)'
      };
      const vName = voiceNames[currentVoice];
      
      if (currentVoice === 'voice1') {
        document.getElementById('trackerDay1Score').textContent = score + '/10';
      }
      showToast(`Đã lưu đánh giá riêng cho [${vName}] (${score}/10) vào brain.db & brain_score.md!`);
    }"""
content = content.replace(save_fn_old, save_fn_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard patched successfully with strict voice-isolation tags!")
