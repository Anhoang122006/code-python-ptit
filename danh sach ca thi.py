n = int(input())

ds = []

for i in range(1, n+1):
    ngay = input().strip()
    gio = input().strip()
    phong = input().strip()

    # tạo mã
    ma = f"C{i:03d}"

    # tách ngày
    d, m, y = map(int, ngay.split('/'))

    # tách giờ
    h, mi = map(int, gio.split(':'))

    # lưu (key sort + data)
    ds.append(((y, m, d, h, mi, ma), ma, ngay, gio, phong))

# sort
ds.sort()

# output
for _, ma, ngay, gio, phong in ds:
    print(ma, ngay, gio, phong)
