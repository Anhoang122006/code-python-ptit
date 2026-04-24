import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    # ma trận ảnh
    a = [list(map(int, input().split())) for _ in range(n)]

    # kernel 3x3
    k = [list(map(int, input().split())) for _ in range(3)]

    total = 0

    # duyệt vị trí hợp lệ
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            val = 0

            # duyệt kernel 3x3
            for u in range(-1, 2):
                for v in range(-1, 2):
                    val += k[u+1][v+1] * a[i+u][j+v]

            total += val

    print(total)
