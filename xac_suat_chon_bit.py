import sys
from math import gcd


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        s = data[idx + 2].decode()
        idx += 3

        prefix = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] + (ch == '1')

        count = 0
        for i, ch in enumerate(s):
            if ch == '1':
                left = i - k
                if left < 0:
                    left = 0
                right = i + k + 1
                if right > n:
                    right = n
                count += prefix[right] - prefix[left]

        total = n * n
        if count == 0:
            out.append('0/1')
        else:
            g = gcd(count, total)
            out.append(f'{count // g}/{total // g}')

    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    solve()
