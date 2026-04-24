n, m = map(int, input().split())
a = list(map(int, input().split()))

res = []

def format_num(x):
    return f"({x})" if x < 0 else str(x)

def dfs(i, expr, value, last):
    if i == n:
        if value == m:
            res.append(expr + "=" + str(m))
        return

    cur = a[i]
    cur_str = format_num(cur)

    # +
    dfs(i + 1,
        expr + "+" + cur_str,
        value + cur,
        cur)

    # -
    dfs(i + 1,
        expr + "-" + cur_str,
        value - cur,
        -cur)

    # *
    dfs(i + 1,
        expr + "*" + cur_str,
        value - last + last * cur,
        last * cur)

# bắt đầu từ phần tử đầu
dfs(1, format_num(a[0]), a[0], a[0])

# output
if res:
    for r in res:
        print(r)
else:
    print("IMPOSSIBLE")
