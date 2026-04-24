t = int(input())

for _ in range(t):
    n, b = map(int, input().split())

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""

    while n > 0:
        res = digits[n % b] + res
        n //= b

    print(res)
