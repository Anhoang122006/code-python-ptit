import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    INF = 10**30

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        # right_min[i] = min(a[i], a[i+1], ..., a[n-1])
        right_min = [INF] * (n + 1)
        for i in range(n - 1, -1, -1):
            right_min[i] = a[i] if a[i] < right_min[i + 1] else right_min[i + 1]

        ans = 0
        left_max = -INF  # max tren doan ben trai

        for i in range(n):
            # Dieu kien:
            # 1) moi phan tu ben trai <= a[i]  <=> left_max <= a[i]
            # 2) moi phan tu ben phai > a[i]   <=> a[i] < min_ben_phai
            if left_max <= a[i] and a[i] < right_min[i + 1]:
                ans += 1
            if a[i] > left_max:
                left_max = a[i]

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
