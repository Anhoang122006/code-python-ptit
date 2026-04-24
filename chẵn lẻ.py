def check(s):

    tong = 0
    for char in s:
        tong += int(char)

    if tong % 10 == 0:
        return True
    return False


def canh(s):

    for i in range(len(s) - 1):

        diff = abs(ord(s[i]) - ord(s[i + 1]))


        if diff !=2:
            return False

    return True


def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        if check(s) and canh(s):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()