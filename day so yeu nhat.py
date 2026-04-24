import sys

def weakness(arr, x):
    # max absolute subarray sum of (arr[i] - x)
    b0 = arr[0] - x
    cur_max = best_max = b0
    cur_min = best_min = b0

    for i in range(1, len(arr)):
        v = arr[i] - x

        cur_max = max(v, cur_max + v)
        if cur_max > best_max:
            best_max = cur_max

        cur_min = min(v, cur_min + v)
        if cur_min < best_min:
            best_min = cur_min

    return max(best_max, -best_min)


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]

    lo = float(min(a))
    hi = float(max(a))

    # F(x) is convex => ternary search on [min(a), max(a)]
    for _ in range(120):
        m1 = lo + (hi - lo) / 3.0
        m2 = hi - (hi - lo) / 3.0

        f1 = weakness(a, m1)
        f2 = weakness(a, m2)

        if f1 > f2:
            lo = m1
        else:
            hi = m2

    x = (lo + hi) / 2.0
    ans = weakness(a, x)
    print(f"{ans:.6f}")


if __name__ == "__main__":
    solve()
