import sys
input = sys.stdin.readline

def calc_cost(s, counts):
    full_xe = 0
    rems = []
    for c in counts:
        full_xe += c // s
        r = c % s
        if r > 0:
            rems.append(r)
    rems.sort()
    lo, hi = 0, len(rems) - 1
    extra = 0
    while lo <= hi:
        if lo == hi:
            extra += 1
            break
        if rems[lo] + rems[hi] <= s:
            extra += 1
            lo += 1
            hi -= 1
        else:
            extra += 1
            hi -= 1
    return (full_xe + extra) * s

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    counts = list(counts.values())

    lo, hi = 1, n
    while hi - lo > 2:
        m1 = lo + (hi - lo) // 3
        m2 = hi - (hi - lo) // 3
        if calc_cost(m1, counts) <= calc_cost(m2, counts):
            hi = m2
        else:
            lo = m1

    best = min(calc_cost(s, counts) for s in range(lo, hi + 1))
    print(best)

solve()
