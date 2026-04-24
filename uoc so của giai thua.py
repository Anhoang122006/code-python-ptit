t = int(input())

for _ in range(t):
    n, p = map(int, input().split())

    res = 0
    power = p

    while power <= n:
        res += n // power
        power *= p

    print(res)
