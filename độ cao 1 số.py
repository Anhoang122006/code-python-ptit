def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

while True:
    line = input().strip()
    if line == "-1":
        break

    n, h = map(int, line.split())

    count = 0
    for i in range(n):
        if digit_sum(i) == h:
            count += 1

    print(count)
