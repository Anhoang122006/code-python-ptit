s1 = input().lower().split()
s2 = input().lower().split()

set1 = set(s1)
set2 = set(s2)

# hợp
union = sorted(set1 | set2)

# giao
inter = sorted(set1 & set2)

print(' '.join(union))
print(' '.join(inter))
