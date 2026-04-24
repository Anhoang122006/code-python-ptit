def digit_sum(n):
    return sum(int(c) for c in str(n))

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            if digit_sum(a[i]) > digit_sum(a[j]) or (digit_sum(a[i]) == digit_sum(a[j]) and a[i] > a[j]):
                a[i], a[j] = a[j], a[i]

    print(*a)
