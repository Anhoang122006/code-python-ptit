def solve():
  t=int(input())
  for _ in range(t):
    s=input()
    n=input()
    i=0
    count=0
    while str.find(n,i)!=-1:
      count+=1
      i=str.find(n,i)+len(n)
    print(count)
solve()
