n = int(input())

ds = []

for _ in range(n):
    ma = input().strip()
    ten = input().strip()
    vao = input().strip()
    ra = input().strip()

    # tách giờ phút
    h1, m1 = map(int, vao.split(":"))
    h2, m2 = map(int, ra.split(":"))

    # đổi về phút
    start = h1 * 60 + m1
    end = h2 * 60 + m2

    tong = end - start

    ds.append((ma, ten, tong))

# sắp xếp giảm dần theo thời gian
ds.sort(key=lambda x: -x[2])

# in kết quả
for ma, ten, tong in ds:
    gio = tong // 60
    phut = tong % 60
    print(ma, ten, gio, "gio", phut, "phut")
