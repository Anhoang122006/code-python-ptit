n, k = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

groups = 1
for i in range(1, n):
    if A[i] - A[i-1] > k:
        groups += 1

print(groups)
