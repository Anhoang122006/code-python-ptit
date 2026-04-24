t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    result = 0

    for x in a:
        result ^= x   # XOR

    print(result)
