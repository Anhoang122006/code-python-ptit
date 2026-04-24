import sys
import re

# đọc toàn bộ input
text = sys.stdin.read()

# tách câu theo . ? !
sentences = re.split(r'[.?!]', text)

for s in sentences:
    # lấy các từ (chữ + số)
    words = re.findall(r'[A-Za-z0-9]+', s)

    if not words:
        continue

    # viết thường hết
    words = [w.lower() for w in words]

    # viết hoa chữ đầu
    words[0] = words[0].capitalize()

    # in ra
    print(' '.join(words))
