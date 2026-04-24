n = int(input())

a = list(map(int, input().split()))

chan = []
le = []

# Bước 1: tách số chẵn và lẻ
for x in a:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

# Bước 2: sắp xếp
chan.sort()              # tăng dần
le.sort(reverse=True)    # giảm dần

# Bước 3: ghép lại
i = 0  # index cho chan
j = 0  # index cho le

result = []

for x in a:
    if x % 2 == 0:
        result.append(chan[i])
        i += 1
    else:
        result.append(le[j])
        j += 1

# In kết quả
print(*result)
