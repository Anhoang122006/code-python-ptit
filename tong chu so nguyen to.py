import math
def check(s):
    if s<2:
        return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True
def solve():
    t=int(input())
    for _ in range(t):
      n=int(input())
      tong=0
      while n>0:
        tong+=n%10
        n//=10
      if check(tong):
        print("YES")
      else:
        print("NO")

if __name__=="__main__":
   solve()
