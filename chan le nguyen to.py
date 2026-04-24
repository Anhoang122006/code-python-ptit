def check(s):
    for i in range(0,len(s),2):
        if int(s[i])%2!=0:
            return False
    for i in range(1,len(s),2):
        if int(s[i])%2==0:
            return False
    m=int(s)
    tong=0
    while m>0:
        tong+=m%10
        m//=10
    if tong<2:
        return False
    for i in range(2,tong):
        if tong%i==0:
            return False
    return True

def solve():
    t=int(input())
    for _ in range(t):
        n=input()
        if check(n):
            print("YES")
        else:
            print("NO")

if __name__=="__main__":
    solve()

