import sys
import math

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    p = 1
    out = []

    for _ in range(t):
        n = int(data[p]); p += 1
        k = int(data[p]); p += 1
        s = data[p].decode(); p += 1

        # prefix[i] = so luong bit 1 trong S[1..i]
        prefix = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            prefix[i] = prefix[i - 1] + (ch == '1')

        fav = 0  # so cap co thu tu (i, j) thoa man
        for i, ch in enumerate(s, 1):
            if ch == '1':
                l = 1 if i - k < 1 else i - k
                r = n if i + k > n else i + k
                fav += prefix[r] - prefix[l - 1]

        total = n * n
        if fav == 0:
            out.append("0/1")
        else:
            g = math.gcd(fav, total)
            out.append(f"{fav // g}/{total // g}")

    sys.stdout.write("\n".join(out))
if __name__ == "__main__":
    solve()
