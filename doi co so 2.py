import sys
def solve():
  t=int(input())
  for _ in range(t):
    b=int(input())
    x=input()
    n=int(x,2)
    if n==0:
      print(0)
      continue
    res=[]
    while n>0:
      res.append(str(n%b))
      n//=b
    print("".join(reversed(res)))
if __name__=="__main__":
  solve()

