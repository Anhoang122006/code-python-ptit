from itertools import combinations

line1 = input().split()
N, K = int(line1[0]), int(line1[1])

names = input().split()

# Loại bỏ trùng lặp, sắp xếp theo thứ tự từ điển
unique_names = sorted(set(names))

# Sinh tất cả tổ hợp K tên
for combo in combinations(unique_names, K):
    print(' '.join(combo))
