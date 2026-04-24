def solve():
n=int(input())
a=map(int,input().split())
for i in range(len(a)-1):
  if a[i]>a[i+1]:
    cnt+=1
print(cnt)
if __name__=="__main__":
  solve()
