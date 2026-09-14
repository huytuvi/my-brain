import re

html_path = '/Users/huybui/Desktop/my-brain/dashboard.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix literal newlines inside double-quoted strings in generateLiveArticle
# Specifically:
# "Lưu ý riêng: " + customPrompt + "\n\n"
# "Điểm mấu chốt: " + customPrompt + "\n\n"
# customPrompt + "\n\n"

html = html.replace(
    '${customPrompt ? "Lưu ý riêng: " + customPrompt + "\n\n" : ""}',
    '${customPrompt ? "Lưu ý riêng: " + customPrompt + "\\n\\n" : ""}'
)

html = html.replace(
    '${customPrompt ? "Điểm mấu chốt: " + customPrompt + "\n\n" : ""}',
    '${customPrompt ? "Điểm mấu chốt: " + customPrompt + "\\n\\n" : ""}'
)

html = html.replace(
    '${customPrompt ? customPrompt + "\n\n" : ""}',
    '${customPrompt ? customPrompt + "\\n\\n" : ""}'
)

# Also check any other \n inside double or single quotes
# Let's inspect
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Replacement done. Validating syntax...")
