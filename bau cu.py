n, m = map(int, input().split())
a = list(map(int, input().split()))

# Đếm phiếu
cnt = {}
for x in a:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

# Lấy các giá trị
values = list(cnt.values())

max1 = max(values)

# Tìm max thứ 2
candidates = []
for v in values:
    if v < max1:
        candidates.append(v)

if len(candidates) == 0:
    print("NONE")
else:
    max2 = max(candidates)

    # tìm ứng viên có phiếu = max2
    result = []
    for k in cnt:
        if cnt[k] == max2:
            result.append(k)

    print(min(result))
