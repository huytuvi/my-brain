file_path = '/Users/huybui/Desktop/my-brain/dashboard.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Header API Key container to support auto-hide
header_ui_old = '''      <!-- Gemini API Key Input Bar -->
      <div class="flex items-center gap-1.5 bg-slate-100 p-1 rounded-xl border border-slate-200">
        <div class="flex items-center pl-2 text-slate-400">
          <i class="fa-solid fa-key text-xs"></i>
        </div>
        <input type="password" id="geminiApiKeyInput" placeholder="Dán Gemini API Key vào đây..." class="bg-white border border-slate-200 rounded-lg px-2.5 py-1 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 w-52 font-mono">
        <button onclick="saveApiKey()" class="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1 shadow-2xs">
          <span>Lưu Key</span>
        </button>
      </div>'''

header_ui_new = '''      <!-- Gemini API Key Bar (Auto-Hide when Saved) -->
      <div id="headerApiBox" class="flex items-center gap-1.5 bg-slate-100 p-1 rounded-xl border border-slate-200">
        <div id="headerApiInputGroup" class="flex items-center gap-1.5">
          <div class="flex items-center pl-2 text-slate-400">
            <i class="fa-solid fa-key text-xs"></i>
          </div>
          <input type="password" id="geminiApiKeyInput" placeholder="Dán Gemini API Key vào đây..." class="bg-white border border-slate-200 rounded-lg px-2.5 py-1 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 w-52 font-mono">
          <button onclick="saveApiKey()" class="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1 shadow-2xs">
            <span>Lưu Key</span>
          </button>
        </div>
        <div id="headerApiLockedGroup" class="hidden items-center gap-2 px-2.5 py-1 text-xs font-semibold text-emerald-800 bg-emerald-50 rounded-lg border border-emerald-200">
          <span class="flex items-center gap-1.5">
            <i class="fa-solid fa-lock text-emerald-600"></i> Gemini AI Đã Khóa Bảo Mật
          </span>
          <button onclick="unlockApiKey()" class="text-[10px] text-slate-400 hover:text-red-600 underline font-normal ml-1">Đổi Key</button>
        </div>
      </div>'''

content = content.replace(header_ui_old, header_ui_new)

# 2. Update Sidebar API Key container to support auto-hide
sidebar_ui_old = '''      <!-- 0. Gemini API Key Card (Very Visible) -->
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
      </div>'''

sidebar_ui_new = '''      <!-- 0. Gemini API Key Card (Auto-Hide when Saved) -->
      <div id="sidebarApiCard" class="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-2xl p-4 shadow-sm space-y-2.5">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-blue-900 flex items-center gap-1.5 uppercase tracking-wide">
            <i class="fa-brands fa-google text-blue-600 text-sm"></i> KẾT NỐI GOOGLE GEMINI AI
          </span>
          <span id="apiStatusBadge" class="text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Đã kết nối
          </span>
        </div>
        <div id="sidebarApiInputGroup" class="space-y-2">
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
        <div id="sidebarApiLockedGroup" class="hidden items-center justify-between p-2.5 bg-white/80 rounded-xl border border-emerald-200 text-xs">
          <span class="text-emerald-800 font-bold flex items-center gap-1.5 text-[11px]">
            <i class="fa-solid fa-shield-check text-emerald-600"></i> Mã API Key đã được bảo mật & ẩn an toàn
          </span>
          <button onclick="unlockApiKey()" class="text-[10px] text-slate-500 hover:text-blue-700 font-semibold underline">Đổi Key</button>
        </div>
      </div>'''

content = content.replace(sidebar_ui_old, sidebar_ui_new)

# 3. Update JavaScript logic to show/hide securely
js_api_old = '''    function updateApiStatus(hasKey) {
      const badge = document.getElementById('apiStatusBadge');
      if (badge) {
        if (hasKey) {
          badge.className = 'text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 flex items-center gap-1';
          badge.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Đã kết nối Gemini AI';
        } else {
          badge.className = 'text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800';
          badge.textContent = 'Chưa có Key (Dùng mẫu)';
        }
      }
    }'''

js_api_new = '''    function updateApiStatus(hasKey) {
      const headerInputGroup = document.getElementById('headerApiInputGroup');
      const headerLockedGroup = document.getElementById('headerApiLockedGroup');
      const sidebarInputGroup = document.getElementById('sidebarApiInputGroup');
      const sidebarLockedGroup = document.getElementById('sidebarApiLockedGroup');
      const badge = document.getElementById('apiStatusBadge');

      if (hasKey) {
        if (headerInputGroup) headerInputGroup.classList.add('hidden');
        if (headerLockedGroup) {
          headerLockedGroup.classList.remove('hidden');
          headerLockedGroup.classList.add('flex');
        }
        if (sidebarInputGroup) sidebarInputGroup.classList.add('hidden');
        if (sidebarLockedGroup) {
          sidebarLockedGroup.classList.remove('hidden');
          sidebarLockedGroup.classList.add('flex');
        }
        if (badge) {
          badge.className = 'text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 flex items-center gap-1';
          badge.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Đã bảo mật & ẩn Key';
        }
      } else {
        if (headerInputGroup) headerInputGroup.classList.remove('hidden');
        if (headerLockedGroup) {
          headerLockedGroup.classList.add('hidden');
          headerLockedGroup.classList.remove('flex');
        }
        if (sidebarInputGroup) sidebarInputGroup.classList.remove('hidden');
        if (sidebarLockedGroup) {
          sidebarLockedGroup.classList.add('hidden');
          sidebarLockedGroup.classList.remove('flex');
        }
        if (badge) {
          badge.className = 'text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800';
          badge.textContent = 'Chưa có Key';
        }
      }
    }

    function unlockApiKey() {
      if (confirm('Bạn có muốn mở lại ô nhập để thay đổi hoặc xóa Gemini API Key?')) {
        localStorage.removeItem('simon_gemini_api_key');
        document.getElementById('geminiApiKeyInput').value = '';
        document.getElementById('geminiApiKeySidebar').value = '';
        updateApiStatus(false);
        showToast('Đã mở khóa. Bạn có thể nhập mã API Key mới.');
      }
    }'''

content = content.replace(js_api_old, js_api_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Auto-hide API key security feature added successfully!")
