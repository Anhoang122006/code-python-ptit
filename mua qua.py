import sys


def build_prefix(arr):
    pref = [0]
    for v in arr:
        pref.append(pref[-1] + v)
    return pref


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def lower_bound(self, target):
        pos = 0
        step = 1 << (self.n.bit_length() - 1)
        cur = 0
        while step:
            nxt = pos + step
            if nxt <= self.n and cur + self.bit[nxt] < target:
                cur += self.bit[nxt]
                pos = nxt
            step >>= 1
        return pos + 1


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    p = 0
    n, m, k = data[p], data[p + 1], data[p + 2]
    p += 3

    costs = [0] + data[p : p + n]
    p += n

    a = data[p]
    p += 1
    ti = set(data[p : p + a])
    p += a

    b = data[p]
    p += 1
    teo = set(data[p : p + b])

    common = []
    other = []

    for i in range(1, n + 1):
        if i in ti and i in teo:
            common.append(costs[i])
        else:
            other.append(costs[i])

    common.sort()
    pref_common = build_prefix(common)

    max_take_common = min(len(common), m)
    if k > max_take_common:
        print(-1)
        return

    # For each t in [k..max_take_common]:
    # pick t cheapest common as mandatory,
    # then pick (m - t) cheapest from remaining pool (common[t:] + other).
    all_values = sorted(set(costs[1:]))
    comp = {v: i + 1 for i, v in enumerate(all_values)}

    bit_cnt = Fenwick(len(all_values))
    bit_sum = Fenwick(len(all_values))

    def add_value(val, delta):
        idx_val = comp[val]
        bit_cnt.add(idx_val, delta)
        bit_sum.add(idx_val, delta * val)

    def sum_k_smallest(need):
        if need == 0:
            return 0
        pos = bit_cnt.lower_bound(need)
        cnt_before = bit_cnt.sum(pos - 1)
        sum_before = bit_sum.sum(pos - 1)
        remain = need - cnt_before
        return sum_before + remain * all_values[pos - 1]

    # Initial pool for t = k: common[k:] + other
    for v in other:
        add_value(v, 1)
    for i in range(k, len(common)):
        add_value(common[i], 1)

    ans = None
    pool_size = len(other) + (len(common) - k)

    for t in range(k, max_take_common + 1):
        need = m - t
        if 0 <= need <= pool_size:
            total = pref_common[t] + sum_k_smallest(need)
            if ans is None or total < ans:
                ans = total

        if t < max_take_common:
            # Move from t to t+1: common[t] becomes mandatory, remove from pool.
            add_value(common[t], -1)
            pool_size -= 1

    print(-1 if ans is None else ans)


if __name__ == "__main__":
    solve()
