s = input().strip()

A = []

i = 0
while i + 1 < len(s):
    num = int(s[i] + s[i+1])
    A.append(num)
    i += 2

# loại trùng + sắp xếp
A = set(A)

for x in A:
    print(x, end=" ")
