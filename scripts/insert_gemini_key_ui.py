with open('/Users/huybui/Desktop/my-brain/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert into Header (right after button Kế Hoạch 21 Bài)
target_header_btn = '''      <!-- Button to Open 7-Day Plan Popup -->
      <button onclick="openPlanModal()" class="px-3.5 py-1.5 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 rounded-xl text-xs font-bold flex items-center gap-2 transition shadow-2xs">
        <i class="fa-solid fa-table-list text-indigo-600"></i>
        <span>Kế Hoạch 21 Bài (7 Ngày)</span>
      </button>'''

replacement_header = '''      <!-- Button to Open 7-Day Plan Popup -->
      <button onclick="openPlanModal()" class="px-3.5 py-1.5 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 rounded-xl text-xs font-bold flex items-center gap-2 transition shadow-2xs">
        <i class="fa-solid fa-table-list text-indigo-600"></i>
        <span>Kế Hoạch 21 Bài (7 Ngày)</span>
      </button>

      <!-- Gemini API Key Input Bar -->
      <div class="flex items-center gap-1.5 bg-slate-100 p-1 rounded-xl border border-slate-200">
        <div class="flex items-center pl-2 text-slate-400">
          <i class="fa-solid fa-key text-xs"></i>
        </div>
        <input type="password" id="geminiApiKeyInput" placeholder="Dán Gemini API Key vào đây..." class="bg-white border border-slate-200 rounded-lg px-2.5 py-1 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 w-52 font-mono">
        <button onclick="saveApiKey()" class="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1 shadow-2xs">
          <span>Lưu Key</span>
        </button>
      </div>'''

content = content.replace(target_header_btn, replacement_header)

# 2. Also add a prominent dedicated Card in Left Sidebar above Brand Voice
target_voice_card = '''    <!-- LEFT PANEL: CONTROLS & COMMAND (Col 4) -->
    <aside class="col-span-12 lg:col-span-4 space-y-4">

      <!-- 1. Brand Voice Selector -->'''

replacement_voice_card = '''    <!-- LEFT PANEL: CONTROLS & COMMAND (Col 4) -->
    <aside class="col-span-12 lg:col-span-4 space-y-4">

      <!-- 0. Gemini API Key Card (Very Visible) -->
      <div class="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-2xl p-4 shadow-sm space-y-2.5">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-blue-900 flex items-center gap-1.5 uppercase tracking-wide">
            <i class="fa-brands fa-google text-blue-600 text-sm"></i> KẾT NỐI GOOGLE GEMINI AI
          </span>
          <span id="apiStatusBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-200 text-slate-600">Chưa kết nối</span>
        </div>
        <p class="text-[11px] text-slate-600 leading-relaxed">
          Lấy mã API miễn phí 100% tại: <a href="https://aistudio.google.com" target="_blank" class="text-blue-700 font-bold underline hover:text-blue-900">aistudio.google.com</a>
        </p>
        <div class="flex gap-1.5">
          <input type="password" id="geminiApiKeySidebar" placeholder="Dán mã API Key vào đây..." class="flex-1 bg-white border border-blue-200 rounded-xl px-3 py-2 text-xs font-mono text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500">
          <button onclick="saveApiKeySidebar()" class="px-3.5 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-xl text-xs font-bold transition flex items-center gap-1 shadow-sm">
            <i class="fa-solid fa-check"></i> Lưu Key
          </button>
        </div>
      </div>

      <!-- 1. Brand Voice Selector -->'''

content = content.replace(target_voice_card, replacement_voice_card)

# 3. Update saveApiKey and checkSavedApiKey to sync both inputs
old_key_funcs = '''    function saveApiKey() {
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
    }'''

new_key_funcs = '''    function updateApiStatus(hasKey) {
      const badge = document.getElementById('apiStatusBadge');
      if (badge) {
        if (hasKey) {
          badge.className = 'text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 flex items-center gap-1';
          badge.innerHTML = '<span class=\"w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse\"></span> Đã kết nối Gemini AI';
        } else {
          badge.className = 'text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800';
          badge.textContent = 'Chưa có Key (Dùng mẫu)';
        }
      }
    }

    function saveApiKey() {
      const k = document.getElementById('geminiApiKeyInput').value.trim();
      if (!k) {
        alert('Vui lòng dán mã Gemini API Key.');
        return;
      }
      localStorage.setItem('simon_gemini_api_key', k);
      const sideInput = document.getElementById('geminiApiKeySidebar');
      if (sideInput) sideInput.value = k;
      updateApiStatus(true);
      showToast('Đã kết nối Google Gemini API thành công! Giờ bạn có thể sinh bài thật 100%!');
    }

    function saveApiKeySidebar() {
      const k = document.getElementById('geminiApiKeySidebar').value.trim();
      if (!k) {
        alert('Vui lòng dán mã Gemini API Key.');
        return;
      }
      localStorage.setItem('simon_gemini_api_key', k);
      const topInput = document.getElementById('geminiApiKeyInput');
      if (topInput) topInput.value = k;
      updateApiStatus(true);
      showToast('Đã kết nối Google Gemini API thành công! Giờ bạn có thể sinh bài thật 100%!');
    }

    function checkSavedApiKey() {
      const saved = localStorage.getItem('simon_gemini_api_key');
      if (saved) {
        const topInput = document.getElementById('geminiApiKeyInput');
        if (topInput) topInput.value = saved;
        const sideInput = document.getElementById('geminiApiKeySidebar');
        if (sideInput) sideInput.value = saved;
        updateApiStatus(true);
      } else {
        updateApiStatus(false);
      }
    }'''

content = content.replace(old_key_funcs, new_key_funcs)

with open('/Users/huybui/Desktop/my-brain/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Both header and sidebar Gemini API inputs inserted successfully!")
