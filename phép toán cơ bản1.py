import itertools

ops = ['+', '-', '*', '/']

def check(expr):
    try:
        left, right = expr.split('=')
        if eval(left) == int(right):
            return True
    except:
        return False
    return False

t = int(input())

for _ in range(t):
    s = input().strip()

    pos = [i for i, c in enumerate(s) if c == '?']

    found = False

    # thử tất cả khả năng
    for repl in itertools.product('0123456789+-*/', repeat=len(pos)):
        temp = list(s)

        for i, ch in zip(pos, repl):
            temp[i] = ch

        expr = ''.join(temp)

        # loại trường hợp sai format (vd: 01, /0,...)
        if "/0" in expr:
            continue

        try:
            left, right = expr.split('=')
            if eval(left) == int(right):
                print(expr)
                found = True
                break
        except:
            continue

    if not found:
        print("WRONG PROBLEM!")
