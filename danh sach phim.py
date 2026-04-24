def parse_date(s):
    d, m, y = map(int, s.split('/'))
    return (y, m, d)

# nhập thể loại
n = int(input())
the_loai = {}

for i in range(1, n+1):
    ma = f"TL{i:03d}"
    ten = input().strip()
    the_loai[ma] = ten

# nhập phim
m = int(input())
ds = []

for i in range(1, m+1):
    ma_phim = f"P{i:03d}"
    ma_tl = input().strip()
    ngay = input().strip()
    ten_phim = input().strip()
    so_tap = input().strip()

    ds.append((
        parse_date(ngay),     # để sort
        ten_phim,
        ma_phim,
        the_loai[ma_tl],
        ngay,
        so_tap
    ))

# sort
ds.sort()

# output
for _, ten_phim, ma, tl, ngay, so_tap in ds:
    print(ma, tl, ngay, ten_phim, so_tap)
