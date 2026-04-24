s = input().strip()
k = int(input())

count = {}

# Bước 1 + 2: cắt + đếm
for i in range(0, len(s) - 1, 2):
    num = int(s[i:i+2])

    if num in count:
        count[num] += 1
    else:
        count[num] = 1

# Bước 3: lọc
result = []
for num in count:
    if count[num] >= k:
        result.append(num)

# Bước 4: sort
result.sort()

# In kết quả
if len(result) == 0:
    print("NOT FOUND")
else:
    for num in result:
        print(num, count[num])
