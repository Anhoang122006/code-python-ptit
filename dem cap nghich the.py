import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]

    # Nen toa do
    vals = sorted(set(a))
    rank = {v: i + 1 for i, v in enumerate(vals)}  # 1-indexed

    m = len(vals)
    bit = [0] * (m + 1)

    def update(i, delta):
        while i <= m:
            bit[i] += delta
            i += i & -i

    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    inv = 0
    seen = 0

    for x in a:
        r = rank[x]
        # so phan tu da thay > x = seen - so phan tu <= x
        inv += seen - query(r)
        update(r, 1)
        seen += 1

    print(inv)

if __name__ == "__main__":
    solve()
