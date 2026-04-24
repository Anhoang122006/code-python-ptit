def solve():
  s=input()
  n=len(s)
  perm=['']*n
  used=[False]*n
  def Try(i):
    for j in range(n):
      if not used[j]:
        perm[i]=s[j]
        used[j]=True
        if i==n-1:
          print("".join(perm))
        else:
          Try(i+1)
        used[j]=False
  Try(0)
if __name__ == "__main__":
  solve()

