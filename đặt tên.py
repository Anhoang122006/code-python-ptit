def backtrack(start, path):
    if len(path) == k:
        print(" ".join(path))
        return

    for i in range(start, len(names)):
        path.append(names[i])
        backtrack(i + 1, path)
        path.pop()


# nhập dữ liệu
n, k = map(int, input().split())
names = input().split()

# loại trùng + sắp xếp
names = sorted(set(names))

# sinh tổ hợp
backtrack(0, [])
