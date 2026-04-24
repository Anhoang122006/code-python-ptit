def solve():
  t=int(input())
  for _ in range(t):
    p,q=map(str,input().split())
    x1=input()
    x2=input()
    low=min(p,q)
    high=max(p,q)
    min_sum=int(x1.replace(high,low)) + int(x2.replace(high,low))
    max_sum=int(x1.replace(low,high)) + int(x2.replace(low,high))
    print(f"{min_sum} {max_sum}")
if __name__=="__main__":
  solve()


