n = int(input())

ds = []

for i in range(n):
    name = input().strip()
    old = int(input())
    new = int(input())

    used = new - old

    # tính tiền
    money = 0

    if used <= 50:
        money = used * 100
        fee = 0.02
    elif used <= 100:
        money = 50 * 100 + (used - 50) * 150
        fee = 0.03
    else:
        money = 50 * 100 + 50 * 150 + (used - 100) * 200
        fee = 0.05

    total = int(money * (1 + fee) + 0.5)  # làm tròn

    code = f"KH{str(i+1).zfill(2)}"

    ds.append((code, name, total))

# sắp xếp giảm dần theo tiền
ds.sort(key=lambda x: -x[2])

# in kết quả
for x in ds:
    print(x[0], x[1], x[2])
