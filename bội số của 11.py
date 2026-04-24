while True:
    s = input().strip()
    if s == "-1":
        break

    even_sum = 0
    odd_sum = 0

    for i in range(len(s)):
        if i % 2 == 0:
            even_sum += int(s[i])
        else:
            odd_sum += int(s[i])

    if (even_sum - odd_sum) % 11 == 0:
        print("YES")
    else:
        print("NO")
