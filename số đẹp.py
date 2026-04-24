def check(n):
    s = str(n)
    m = len(s)

    if m % 2 != 0:
        return False

    for i in range(m // 2):
        if s[i] != s[m - i - 1]:
            return False

    for char in s:
        if char not in '02468':
            return False

    return True


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())

        for nums in range(22, n ,2 ):  # Bắt đầu từ 22 vì số đẹp nhỏ nhất là 22

            if check(nums):
                print(nums, end=" ")
        print()


if __name__ == "__main__":
    solve()