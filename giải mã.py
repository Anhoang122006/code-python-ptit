def solve():
    t=int(input())
    for _ in range(t):
        s=input()
        count=0
        ans=""
        for i in range(len(s)-1):
           if s[i+1].isdigit():
               so=int(s[i+1])
               count+=so
               for j in range(so):
                   ans+=s[i]
           count-=so

        print(ans)

if __name__=="__main__":
    solve()
