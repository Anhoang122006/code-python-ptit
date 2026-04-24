import sys
input = sys.stdin.readline

MOD = 10**9 + 7

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    maxf = N + K + 10
    fact = [1] * maxf
    for i in range(1, maxf):
        fact[i] = fact[i-1] * i % MOD
    inv_fact = [1] * maxf
    inv_fact[maxf-1] = pow(fact[maxf-1], MOD-2, MOD)
    for i in range(maxf-2, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    def C(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

    ans = 0
    for i, a in enumerate(A):
        coef = (C(i, K-1) - C(N-1-i, K-1)) % MOD
        ans = (ans + a * coef) % MOD

    print(ans % MOD)

solve()
