import sys


def solve():
    input = sys.stdin.buffer.readline

    first = input().strip()
    while not first:
        first = input().strip()
    n = int(first)

    tong_input = 0
    need = n - 1
    cnt = 0

    while cnt < need:
        line = input()
        if not line:
            break
        for x in map(int, line.split()):
            tong_input += x
            cnt += 1
            if cnt == need:
                break

    tong_day_du = n * (n + 1) // 2
    sys.stdout.write(str(tong_day_du - tong_input))


if __name__ == "__main__":
    solve()
