def to_base3(n):
    # chuyển số thập phân sang chuỗi hệ 3
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s


def is_dominant_2(s):
    # kiểm tra số lượng '2' > 50%
    count_2 = s.count('2')
    return count_2 > len(s) / 2


t = int(input())

for _ in range(t):
    n = int(input())

    result = []
    num = 1

    while len(result) < n:
        base3 = to_base3(num)

        if is_dominant_2(base3):
            result.append(base3)

        num += 1

    print(" ".join(result))
