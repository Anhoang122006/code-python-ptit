t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ok = True

    for i in range(n - 1):
        if a[i] == a[i + 1]:
            ok = False
            break

    print("YES" if ok else "NO")
