import sys
def solve():
 t=int(input())
 for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  a.sort()
  b.sort()
  ok=True
  for i in range(n):
    if a[i]>b[i]:
      ok=False
      break
  if ok==True:
    print("YES")
  else:
    print("NO")

if __name__=="__main__":
  solve()
