def check(s):
    n=s[::-1]
    for i in range(1,len(s)):
      if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(n[i])-ord(n[i-1])):
         return False
    return True


def solve():
  t=int(input())
  for _ in range(t):
      k=input()
      if check(k):
          print("YES")
      else:
          print("NO")

if __name__ == "__main__":
    solve()
