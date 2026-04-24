def normalize(s):
    # bỏ số 0 ở đầu
    while len(s) > 1 and s[0] == '0':
        s = s[1:]
    return s

def smaller(a, b):
    # so sánh a < b
    if len(a) != len(b):
        return len(a) < len(b)
    return a < b

while True:
    n = int(input())
    if n == 0:
        break

    arr = []

    for i in range(n):
        s = input().strip()
        s = normalize(s)
        arr.append(s)

    mn = arr[0]
    mx = arr[0]
    all_equal = True

    for i in range(1, n):
        if arr[i] != arr[0]:
            all_equal = False

        if smaller(arr[i], mn):
            mn = arr[i]

        if smaller(mx, arr[i]):
            mx = arr[i]

    if all_equal:
        print("BANG NHAU")
    else:
        print(mn, mx)
