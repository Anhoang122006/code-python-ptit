import sys

def ones_upto(n: int) -> int:
    """Tong so bit 1 trong cac so tu 0..n."""
    if n <= 0:
        return 0
    total = 0
    m = n + 1
    bit = 0
    while (1 << bit) <= n:
        half = 1 << bit
        cycle = half << 1
        full_cycles = m // cycle
        rem = m % cycle
        total += full_cycles * half + max(0, rem - half)
        bit += 1
    return total

def ones_in_range(l: int, r: int) -> int:
    if l > r:
        return 0
    return ones_upto(r) - ones_upto(l - 1)

def weighted_prefix(n: int) -> float:
    """
    S(n) = sum_{x=1..n} popcount(x)/bit_length(x)
    """
    if n <= 0:
        return 0.0

    res = 0.0
    max_len = n.bit_length()

    for length in range(1, max_len + 1):
        left = 1 << (length - 1)
        right = min(n, (1 << length) - 1)
        if left > right:
            continue
        total_ones = ones_in_range(left, right)
        res += total_ones / length

    return res

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        total_numbers = b - a + 1
        good = weighted_prefix(b) - weighted_prefix(a - 1)
        ans = good / total_numbers
        out.append(f"{ans:.5f}")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
