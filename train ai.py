import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    U = float(input())
    P = list(map(float, input().split()))
    P.sort()

    # Nâng đều các module từ thấp lên cao
    for i in range(N):
        # Muốn nâng P[0..i] lên bằng P[i+1] (hoặc target nếu i == N-1)
        target = P[i+1] if i < N-1 else 1.0

        # Cần (i+1) * (target - P[i]) thời gian để nâng i+1 module đầu lên target
        needed = (i + 1) * (target - P[i])

        if U <= needed:
            # Dừng ở đây, nâng đều (i+1) module lên thêm U/(i+1)
            boost = U / (i + 1)
            for j in range(i + 1):
                P[j] += boost
            break
        else:
            U -= needed
            for j in range(i + 1):
                P[j] = target

    result = 1.0
    for p in P:
        result *= min(p, 1.0)

    print(f"{result:.6f}")

T = int(input())
for _ in range(T):
    solve()
