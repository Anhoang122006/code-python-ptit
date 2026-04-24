
m = int(input("m = "))
v = int(input("v = "))
t = int(input("t = "))
d = input("d = ")


quang_duong = v * t



if d == 'C':
    vi_tri = quang_duong % m
else:
    vi_tri = (-quang_duong) % m

print("Result =", vi_tri)
