import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))

    # sắp xếp giảm dần
    a.sort(reverse=True)

    # prefix sum
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]

    # cách 1
    if c + d <= n:
        sum1 = prefix[c]          # top C
        sum2 = prefix[c + d] - prefix[c]  # next D
        ans1 = sum1 / c + sum2 / d
    else:
        ans1 = 0

    # cách 2 (đảo C và D)
    if c + d <= n:
        sum1 = prefix[d]
        sum2 = prefix[c + d] - prefix[d]
        ans2 = sum1 / d + sum2 / c
    else:
        ans2 = 0

    print(f"{max(ans1, ans2):.6f}")
