import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]

    cur = set()      # OR cua cac day con ket thuc tai vi tri hien tai
    all_vals = set() # tap gia tri OR cua moi day con

    for x in a:
        # Day con moi: chi gom x, hoac noi x vao cac day con truoc do
        nxt = {x}
        for v in cur:
            nxt.add(v | x)

        cur = nxt
        all_vals.update(cur)

    print(len(all_vals))

if __name__ == "__main__":
    solve()
