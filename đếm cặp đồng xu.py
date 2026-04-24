n = int(input())

grid = []
for _ in range(n):
    grid.append(input().strip())

result = 0

# đếm theo hàng
for i in range(n):
    count = grid[i].count('C')
    result += count * (count - 1) // 2

# đếm theo cột
for j in range(n):
    count = 0
    for i in range(n):
        if grid[i][j] == 'C':
            count += 1
    result += count * (count - 1) // 2

print(result)
