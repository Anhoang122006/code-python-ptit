n = int(input())
a = [int(input()) for _ in range(n)]

stack = []
res = 0

for x in a:
    while stack and stack[-1] < x:
        stack.pop()

    res += len(stack)
    stack.append(x)

print(res)
