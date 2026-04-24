import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    # Khởi tạo 3 số nhỏ nhất bằng vô cực
    min1 = min2 = min3 = float('inf')

    for x in A:
        if x <= min1:           # Nhỏ hơn cả min1
            min3 = min2
            min2 = min1
            min1 = x
        elif x <= min2:         # Nhỏ hơn min2 nhưng lớn hơn min1
            min3 = min2
            min2 = x
        elif x <= min3:         # Nhỏ hơn min3
            min3 = x

    out.append(str(min1 + min2 + min3))

sys.stdout.write("\n".join(out) + "\n")
