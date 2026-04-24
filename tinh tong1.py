import sys
input = sys.stdin.readline

MOD = 10**9 + 7

def modinv(a, m=MOD):
    return pow(a, m-2, m)

def lagrange_interpolation(x_val, y, MOD):
    """
    Nội suy Lagrange tại x_val, biết y[i] = f(i+1) với i = 0..m-1
    Các điểm x là 1, 2, ..., m (liên tiếp) -> tối ưu O(m)
    """
    m = len(y)
    x_val %= MOD

    # Nếu x_val nằm trong các điểm đã biết
    if 1 <= x_val <= m:
        return y[x_val - 1] % MOD

    # prefix[i] = (x_val-1)*(x_val-2)*...*(x_val-i)
    prefix = [1] * (m + 1)
    for i in range(1, m + 1):
        prefix[i] = prefix[i-1] * (x_val - i) % MOD

    # suffix[i] = (x_val-(i+1))*(x_val-(i+2))*...*(x_val-m)
    suffix = [1] * (m + 2)
    for i in range(m - 1, -1, -1):
        suffix[i] = suffix[i+1] * (x_val - (i+1)) % MOD

    # Tiền tính giai thừa và nghịch đảo
    fact = [1] * (m + 1)
    for i in range(1, m + 1):
        fact[i] = fact[i-1] * i % MOD

    ans = 0
    for i in range(m):
        xi = i + 1  # điểm x thứ i là xi = i+1
        # numerator = product of (x_val - xj) for j != i
        num = prefix[i] * suffix[i+1] % MOD
        # denominator = product of (xi - xj) for j != i
        # = (i)! * (-1)^(m-1-i) * (m-1-i)!
        denom = fact[i] * fact[m - 1 - i] % MOD
        if (m - 1 - i) % 2 == 1:
            denom = MOD - denom
        ans = (ans + y[i] * num % MOD * modinv(denom)) % MOD

    return ans

def solve():
    n, K = map(int, input().split())
    MOD = 10**9 + 7

    m = K + 2  # cần K+2 điểm để xác định đa thức bậc K+1

    # Tính y[i] = 1^K + 2^K + ... + (i+1)^K với i = 0..m-1
    # Tức là prefix sum tại các điểm 1, 2, ..., m
    y = []
    running = 0
    for i in range(1, m + 1):
        running = (running + pow(i, K, MOD)) % MOD
        y.append(running)

    # Nội suy tại n
    ans = lagrange_interpolation(n % MOD, y, MOD)
    print(ans)

T = int(input())
for _ in range(T):
    solve()
