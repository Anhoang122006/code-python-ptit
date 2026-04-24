import sys

MOD = 1000

def mat_mul(a, b):
    return [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD,
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD,
        ],
    ]

def mat_pow(mat, exp):
    res = [[1, 0], [0, 1]]  # identity
    while exp > 0:
        if exp & 1:
            res = mat_mul(res, mat)
        mat = mat_mul(mat, mat)
        exp >>= 1
    return res

def calc_last3(n):
    # s_n = (3+sqrt(5))^n + (3-sqrt(5))^n
    # s_0 = 2, s_1 = 6, s_n = 6*s_{n-1} - 4*s_{n-2}
    if n == 0:
        s_n = 2
    elif n == 1:
        s_n = 6
    else:
        M = [[6, MOD - 4], [1, 0]]  # -4 mod 1000 = 996
        P = mat_pow(M, n - 1)
        s1, s0 = 6, 2
        s_n = (P[0][0] * s1 + P[0][1] * s0) % MOD

    # floor((3+sqrt(5))^n) = s_n - 1 (for n >= 1), đề chỉ dùng n >= 1
    ans = (s_n - 1) % MOD
    return f"{ans:03d}"

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        out.append(f"Case #{i}: {calc_last3(n)}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
