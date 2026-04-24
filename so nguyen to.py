import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    k = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            k += 1
    print("YES" if is_prime(k) else "NO")