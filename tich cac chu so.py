def digit_product(n):
    p = 1
    for c in str(n):
        p *= int(c)
    return p

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            if digit_product(a[i]) > digit_product(a[j]) or (digit_product(a[i]) == digit_product(a[j]) and a[i] > a[j]):
                a[i], a[j] = a[j], a[i]

    print(*a)
