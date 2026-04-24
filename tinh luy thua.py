import sys
input = sys.stdin.readline

def euler_phi(n):
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result

def pow_mod_general(a, exp, m):
    if m == 1:
        return 0
    return pow(a, exp, m)

def solve(a, b, c, d, M):
    if M == 1:
        return 0
    if a == 0:
        if b == 0:
            return 1 % M
        return 0

    exp1 = b * pow(c, d)

    phi = euler_phi(M)

    cd = pow(c, d, phi) if phi > 0 else 0
    bcd_mod = b * cd % phi

    bcd_real = b * (c ** d)

    if bcd_real >= phi:
        exp = bcd_mod + phi
    else:
        exp = bcd_real

    return pow(a, exp, M)

T = int(input())
out = []
for _ in range(T):
    a, b, c, d, M = map(int, input().split())
    out.append(str(solve(a, b, c, d, M)))
print('\n'.join(out))
