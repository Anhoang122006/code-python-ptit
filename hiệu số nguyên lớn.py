A = input().strip()
B = input().strip()

# Xử lý dấu âm: nếu A < B thì đổi chỗ và thêm dấu -
neg = False
# So sánh sau khi bỏ số 0 đầu
a_clean = A.lstrip('0') or '0'
b_clean = B.lstrip('0') or '0'

if len(a_clean) < len(b_clean) or (len(a_clean) == len(b_clean) and a_clean < b_clean):
    neg = True
    A, B = B, A

A = A[::-1]
B = B[::-1]

result = []
borrow = 0

for i in range(len(A)):
    da = int(A[i])
    db = int(B[i]) if i < len(B) else 0
    diff = da - db - borrow
    if diff < 0:
        diff += 10
        borrow = 1
    else:
        borrow = 0
    result.append(str(diff))

ans = ''.join(result[::-1]).lstrip('0') or '0'

if neg and ans != '0':
    ans = '-' + ans

print(ans)
