import math


def check(s):
    m = s[::-1]
    res=math.gcd(int(m),int(s))
    if res!=1:
        return False
    else:
        return True
def solve():
    t=int(input())
    for _ in range(t):
        s=input()
        if check(s):
            print("YES")
        else:
            print("NO")
if __name__=="__main__":
    solve()

