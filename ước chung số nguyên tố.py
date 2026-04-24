import math
def check(m):
    if m<2:
        return False
    else:
        for i in range(2,int(math.sqrt(m))+1):
            if m%i==0:
                return False


        return True

def sums_n(n):
    digit_sum=0
    while n>0:
        digit_sum+=n%10
        n//=10
    return digit_sum

def solve():
    t=int(input())
    for _ in range(t):
      a,b=map(int,input().split())
      ans=math.gcd(a,b)
      ans1=sums_n(ans)
      if check(ans1):
          print("YES")
      else:
          print("NO")

if __name__=="__main__":
    solve()