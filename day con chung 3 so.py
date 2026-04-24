import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    result = []
    i = j = k = 0

    while i < N and j < M and k < K:
        a, b, c = A[i], B[j], C[k]

        if a == b == c:
            result.append(a)
            i += 1
            j += 1
            k += 1
        else:
            min_val = min(a, b, c)
            if a == min_val:
                i += 1
            if b == min_val:
                j += 1
            if c == min_val:
                k += 1

    if result:
        print(' '.join(map(str, result)))
    else:
        print("NO")
