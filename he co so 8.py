s = input().strip()

# thêm 0 vào đầu cho đủ bội số của 3
while len(s) % 3 != 0:
    s = '0' + s

res = ""

# duyệt từng nhóm 3
for i in range(0, len(s), 3):
    group = s[i:i+3]
    val = int(group, 2)  # chuyển nhị phân -> thập phân
    res += str(val)

print(res)
