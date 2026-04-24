import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# tính chênh lệch
diff = [b[i] - a[i] for i in range(n)]

# sắp xếp giảm dần
diff.sort(reverse=True)

# tổng nếu mua hết sau khuyến mãi
total = sum(b)

# trừ đi lợi ích của K món tốt nhất
for i in range(k):
    total -= diff[i]

print(total)
