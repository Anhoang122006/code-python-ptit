def solve():
  s=input()
  while len(s)%3!=0:
    s="0"+s
  ans=""
  for i in range(0,len(s),3):
    temp=s[i:i+3]
    so_tp=int(temp,2)
    ans=ans+str(so_tp)
  print(ans)
if __name__=="__main__":
  solve()
