n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = set(a)
B = set(b)

# Giao
giao = sorted(A & B)

# A - B
a_tru_b = sorted(A - B)

# B - A
b_tru_a = sorted(B - A)

print(*giao)
print(*a_tru_b)
print(*b_tru_a)
