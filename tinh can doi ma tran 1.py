n = int(input())

a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

k = int(input())

sum_tren = 0
sum_duoi = 0

for i in range(n):
    for j in range(n):
        if j > i:
            sum_tren += a[i][j]
        elif j < i:
            sum_duoi += a[i][j]

# độ chênh lệch
diff = abs(sum_tren - sum_duoi)

# kiểm tra
if diff <= k:
    print("YES")
else:
    print("NO")

print(diff)
