def check(s):
  if len(s)<1:
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
    m=str(tong)
    if check(m) and m==m[::-1]:
      print("YES")
    else:
      print("NO")

if __name__=="__main__":
  solve()
