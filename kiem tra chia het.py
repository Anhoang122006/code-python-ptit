from itertools import combinations

def dem(x, primes):
    # Đếm số trong [1, x] không chia hết cho bất kỳ số nào trong primes
    # Dùng inclusion-exclusion
    n = len(primes)
    cnt = x
    for r in range(1, n + 1):
        for combo in combinations(primes, r):
            tich = 1
            for p in combo:
                tich *= p
            if r % 2 == 1:
                cnt -= x // tich
            else:
                cnt += x // tich
    return cnt

while True:
    line = input().split()
    if line[0] == '-1':
        break
    l, r = int(line[0]), int(line[1])
    n = int(input())

    # Lấy các số nguyên tố trong [2, N]
    primes = []
    for p in range(2, n + 1):
        ok = True
        for d in range(2, p):
            if p % d == 0:
                ok = False
                break
        if ok:
            primes.append(p)

    # Đếm trong [L, R] = đếm trong [1, R] - đếm trong [1, L-1]
    ket_qua = dem(r, primes) - dem(l - 1, primes)
    print(ket_qua)
