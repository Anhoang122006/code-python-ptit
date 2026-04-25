A = input().strip()[::-1]
B = input().strip()[::-1]

result = []
carry = 0

for i in range(max(len(A), len(B))):
    da = int(A[i]) if i < len(A) else 0
    db = int(B[i]) if i < len(B) else 0
    tong = da + db + carry
    result.append(str(tong % 10))
    carry = tong // 10

if carry:
    result.append(str(carry))

print(''.join(result[::-1]).lstrip('0') or '0')
