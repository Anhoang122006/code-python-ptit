def solve():
    t=int(input())
    for _ in range(t):
        n=int(input())
        if n%2==0:
            start=2
        else:
            start=1
        sum=0.0
        for i in range(start,n+1,2):
            sum+=1/i
        print(f"{sum:.6f}")
if __name__=="__main__":
    solve()
