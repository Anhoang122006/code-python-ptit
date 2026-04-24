T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    result = 0
    for x in nums:
        result ^= x

    print(result)
