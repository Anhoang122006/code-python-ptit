t = int(input())

for _ in range(t):
    N = int(input())
    count = 0

    k = 2
    while k * (k - 1) // 2 < N:
        t_val = N - k * (k - 1) // 2

        if t_val % k == 0:
            a = t_val // k
            if a > 0:
                count += 1

        k += 1

    print(count)
