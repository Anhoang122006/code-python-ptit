import sys
from math import isqrt
input = sys.stdin.readline

def bsgs(a, b, M):
    a %= M
    b %= M

    if b == 1:
        return 0

    m = isqrt(M) + 1

    table = {}
    aj = 1
    for j in range(m):
        if aj not in table:
            table[aj] = j
        aj = aj * a % M

    am = pow(a, m, M)
    am_inv = pow(am, -1, M)

    cur = b
    for i in range(1, m + 2):
        cur = cur * am_inv % M
        if cur in table:
            x = i * m + table[cur]
            if x > 0:
                return x

    return -1

T = int(input())
for _ in range(T):
    a, b, M = map(int, input().split())
    print(bsgs(a, b, M))
