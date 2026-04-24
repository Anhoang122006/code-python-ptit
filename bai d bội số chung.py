import sys
input = sys.stdin.readline

MOD = 10**9 + 7
MAXN = 10**6

# SPF (smallest prime factor)
spf = list(range(MAXN + 1))
for i in range(2, int(MAXN**0.5) + 1):
    if spf[i] == i:
        for j in range(i*i, MAXN + 1, i):
            if spf[j] == j:
                spf[j] = i

def factor_count(x, cnt):
    while x > 1:
        p = spf[x]
        cnt[p] = cnt.get(p, 0) + 1
        x //= p

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    cnt = {}

    # phân tích từ a → b
    for i in range(a, b + 1):
        x = i
        while x > 1:
            p = spf[x]
            cnt[p] = cnt.get(p, 0) + 1
            x //= p

    # tính kết quả
    res = 1
    for e in cnt.values():
        res = res * (2 * e + 1) % MOD

    print(res)
