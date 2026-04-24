n = int(input())

def convert(s):
    if '.' in s:
        return float(s)
    return float(s) / 10

def classify(avg):
    if avg < 5:
        return "TRUOT"
    elif avg < 8:
        return "CAN NHAC"
    elif avg <= 9.5:
        return "DAT"
    else:
        return "XUAT SAC"

ds = []

for i in range(n):
    name = input().strip()
    lt = convert(input().strip())
    th = convert(input().strip())

    avg = (lt + th) / 2
    code = f"TS{str(i+1).zfill(2)}"
    loai = classify(avg)

    ds.append((code, name, avg, loai))

# sort giảm dần theo avg
ds.sort(key=lambda x: -x[2])

# in
for x in ds:
    print(x[0], x[1], f"{x[2]:.2f}", x[3])
