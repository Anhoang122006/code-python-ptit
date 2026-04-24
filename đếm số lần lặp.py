s = input().strip()

order = []   # lưu thứ tự xuất hiện
count = {}   # đếm số lần

i = 0
while i + 1 < len(s):
    num = int(s[i] + s[i+1])

    # nếu chưa có thì thêm vào order
    if num not in count:
        order.append(num)
        count[num] = 1
    else:
        count[num] += 1

    i += 2

# in kết quả
for x in order:
    print(x, count[x])
