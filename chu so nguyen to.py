from itertools import product

N = int(input())

digits = ['2', '3', '5', '7']

for length in range(4, N + 1):
    for p in product(digits, repeat=length):
        s = ''.join(p)

        # điều kiện 2: có đủ 2,3,5,7
        if not all(d in s for d in digits):
            continue

        # điều kiện 3: không chẵn
        if s[-1] == '2':
            continue

        print(s)
