n = int(input())
a = list(map(int, input().split()))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# B1: lấy các số nguyên tố
primes = []
for x in a:
    if is_prime(x):
        primes.append(x)

# B2: sắp xếp
primes.sort()

# B3: gán lại
i = 0
for idx in range(len(a)):
    if is_prime(a[idx]):
        a[idx] = primes[i]
        i += 1

print(*a)
