b = input().strip()

# Thêm '0' vào đầu cho đủ bội số của 3
while len(b) % 3 != 0:
    b = '0' + b

result = ''
for i in range(0, len(b), 3):
    group = b[i:i+3]
    octal_digit = int(group, 2)  # chuyển 3 bit nhị phân → số
    result += str(octal_digit)

print(result)
