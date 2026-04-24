while True:
    y, z = map(int, input().split())
    if y == -1:
        break

    # tính tổng chữ số của y
    S = 0
    temp = y
    while temp > 0:
        S += temp % 10
        temp //= 10

    # kiểm tra
    if S == 0 or z % S != 0:
        print(-1)  # hoặc tùy đề yêu cầu
    else:
        print(z // S)
