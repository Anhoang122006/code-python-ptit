s = input()
while len(s) > 1:
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]
    s = str(int(left) + int(right))  # cộng hai nửa, ra kết quả mới
    print(s)
