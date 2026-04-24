def check(s1):
    m=len(s1)
    if s1[m-1]!='6' or s1[m-2]!='8':
        return False
    else:
        return True


def solve():
    t=int(input())
    for _ in range(t):
        n=input()
        if check(n):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
