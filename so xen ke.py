def check(s):
  if len(s) < 3 or len(s) % 2 == 0:
        return False
  if s[0]==s[1]:
    return False
  for i in range(0,len(s),2):
    if s[i]!=s[0]:
      return False
  return True
def solve():
  t=int(input())
  for _ in range(t):
      s=input()
  if check(s):
    print("YES")
  else:
    print("NO")
if __name__=="__main__":
  solve()
