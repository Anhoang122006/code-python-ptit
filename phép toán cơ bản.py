def matches(template, value):
    """Kiểm tra chuỗi value có khớp template (? là wildcard) không"""
    s = str(value)
    if len(s) != len(template):
        return False
    for t, v in zip(template, s):
        if t != '?' and t != v:
            return False
    return True

def solve(expr):
    # Parse: "A op B = C"
    parts = expr.split()
    # parts = [A, op, B, '=', C]
    tA, op, tB, _, tC = parts

    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b if b != 0 and a % b == 0 else None,
    }

    results = []

    # Duyệt tất cả số nguyên dương 2 chữ số: 10 -> 99
    for a in range(10, 100):
        if not matches(tA, a):
            continue
        for b in range(10, 100):
            if not matches(tB, b):
                continue
            if op not in ops:
                continue
            c = ops[op](a, b)
            if c is None:
                continue
            if 10 <= c <= 99 and matches(tC, c):
                results.append((a, b, c))

    if len(results) == 1:
        a, b, c = results[0]
        return f"{a} {op} {b} = {c}"
    else:
        return "WRONG PROBLEM!"

T = int(input())
for _ in range(T):
    expr = input().strip()
    print(solve(expr))
