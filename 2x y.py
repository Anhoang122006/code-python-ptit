import sys
import math

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2

        a = data[idx:idx + n]
        idx += n

        base = a[0]
        g = 0
        for x in a[1:]:
            g = math.gcd(g, abs(x - base))

        # g == 0 <=> tat ca phan tu ban dau bang nhau
        if g == 0:
            out.append("YES" if k == base else "NO")
        else:
            out.append("YES" if (k - base) % g == 0 else "NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
