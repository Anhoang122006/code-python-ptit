def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

n = int(input())
A = list(map(int, input().split()))

# Tạo B: loại trùng giữ thứ tự
seen = set()
B = []
for x in A:
    if x not in seen:
        seen.add(x)
        B.append(x)

m = len(B)

# Tính prefix sum
prefix = [0] * m
prefix[0] = B[0]
for i in range(1, m):
    prefix[i] = prefix[i-1] + B[i]

# Tìm i thỏa mãn
found = False
for i in range(m - 1):
    left = prefix[i]
    right = prefix[m-1] - prefix[i]
    if is_prime(left) and is_prime(right):
        print(i)
        found = True
        break

if not found:
    print("NOT FOUND")
