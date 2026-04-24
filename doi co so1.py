bang_chu_cai="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def solve():
  t=int(input())
  for _ in range(t):
    n,b=map(int,input().split())
    if n==0:
      print("0")
      continue
    ans=""
    while n>0:
      so_du=n%b
      ans=bang_chu_cai[so_du]+ans
      n=n//b
    print(ans)
if __name__=="__main__":
  solve()

