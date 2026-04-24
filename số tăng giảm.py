def check(s):
    if len(s)<3:
        return False
    i=0
    n=len(s)
    while i< n-1 and s[i+1]>s[i]:
        i+=1
    if i==0 or i==n-1:
        return False
    while i<n-1 and s[i+1]<s[i]:
        i+=1
    return i==n-1
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