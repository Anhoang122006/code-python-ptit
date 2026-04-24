t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    def check(x):
        rows = 0
        carry = 0

        for i in range(n):
            total = c[i] + carry
            rows += total // x
            carry = total % x

        return rows >= k

    left, right = 1, sum(c)
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    print(ans * k)
