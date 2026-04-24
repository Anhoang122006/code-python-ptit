def solve():
    a,k,n=map(int,input().split())
    b_min=k-(a%k)
    limit=n-a
    if b_min>limit:
        print("-1")
    else:
        for i in range(b_min,limit+1,k):
            print(i,end=" ")

if __name__=="__main__":
    solve()