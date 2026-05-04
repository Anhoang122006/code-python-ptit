def solve():
  a=input().strip()
  res=[]
  i=0
  while i+1 < len(a):
    num=int(a[i]+a[i+1])
    res.append(num)
    i+=2

  seen=set()
  uniq=[]
  for x in res:
    if x not in seen:
      uniq.append(x)
      seen.add(x)
  for x in uniq:
    print(x,end=" ")
if __name__=="__main__":
  solve()
