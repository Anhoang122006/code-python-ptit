t = int(input())
for _ in range(t):
    n = int(input())
    p = 10
    while n >= p:
        r = n % p
        n = n - r
        if r >= p // 2:
            n += p
        p *= 10
    print(n)