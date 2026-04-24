import sys
input = sys.stdin.readline

n = int(input())

students = []

for _ in range(n):
    name = input().strip()
    c, t = map(int, input().split())
    students.append((name, c, t))

# sort theo yêu cầu
students.sort(key=lambda x: (-x[1], x[2], x[0]))

# in kết quả
for name, c, t in students:
    print(name, c, t)
