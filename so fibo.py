def solve():
    fibo=[0,1,1]
    for i in range(3,93):
        so_moi=fibo[i-1]+fibo[i-2]
        fibo.append(so_moi)
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        ans=[]
        for i in range(a,b+1):
            ans.append(str(fibo[i]))
        print("".join(ans))
if __name__=="__main__":
    solve()
