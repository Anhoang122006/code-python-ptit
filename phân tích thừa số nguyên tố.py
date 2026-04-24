import math
def solve():
    t=int(input())
    for _ in range(t):
      n=int(input())
      print("1",end=" ")
      can=int(math.sqrt(n))
      for i in range(2,can+1):
          if n%i==0:
              count=0
              while n%i==0:
                  count+=1
                  n//=i
              print(f"* {i}^{count}",end=" ")
      if n>1:
          print(f"* {n}^1",end=" ")
      print()
if __name__=="__main__":
   solve()