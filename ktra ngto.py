def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    result = []
    for x in row:
        if is_prime(x):
            result.append(1)
        else:
            result.append(0)
    print(*result)
