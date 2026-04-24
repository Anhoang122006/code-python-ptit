import sys
input = sys.stdin.readline

n = int(input())

students = []

for i in range(1, n + 1):
    name = input().strip()
    scores = list(map(float, input().split()))

    # tính điểm TB
    tb = (scores[0]*2 + scores[1]*2 + sum(scores[2:])) / 12

    # làm tròn 1 chữ số
    tb_round = round(tb + 1e-8, 1)

    # xếp loại
    if tb >= 9:
        rank = "XUAT SAC"
    elif tb >= 8:
        rank = "GIOI"
    elif tb >= 7:
        rank = "KHA"
    elif tb >= 5:
        rank = "TB"
    else:
        rank = "YEU"

    # mã HS
    code = f"HS{i:02d}"

    students.append((code, name, tb_round, rank))

# sort
students.sort(key=lambda x: (-x[2], x[0]))

# output
for code, name, tb, rank in students:
    print(code, name, f"{tb:.1f}", rank)
