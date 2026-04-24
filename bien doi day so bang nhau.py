n = int(input())
a = list(map(int, input().split()))

min_steps = 10**18  # số rất lớn
best_value = a[0]

for i in range(n):
    x = a[i]
    steps = 0

    for j in range(n):
        steps += abs(a[j] - x)

    if steps < min_steps:
        min_steps = steps
        best_value = x

print(min_steps, best_value)
