import math
def solve():
    n,k=map(int,input().split())
    max=int(10**k)
    min=int(10**(k-1))
    count = 0
    for i in range(min,max):

        res=math.gcd(i,n)
        if res==1:
            count+=1
            print(i,end=" ")
        if (count == 10):
            print()
            count=0
if __name__=="__main__":
    solve()
