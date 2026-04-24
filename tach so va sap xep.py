n = int(input())
nums = []

for _ in range(n):
    s = input()
    cur = ""

    for c in s:
        if c.isdigit():
            cur += c
        else:
            if cur != "":
                nums.append(int(cur))
                cur = ""

    # nếu chuỗi kết thúc bằng số
    if cur != "":
        nums.append(int(cur))

# sắp xếp
nums.sort()

# in kết quả
for x in nums:
    print(x)
