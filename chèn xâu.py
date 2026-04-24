s1 = input()
s2 = input()
p = int(input())

# chèn tại vị trí p (1-based)
result = s1[:p-1] + s2 + s1[p-1:]

print(result)
