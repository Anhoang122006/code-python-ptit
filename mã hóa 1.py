def solve():
    t=int(input())
    for _ in range(t):
        s=input()
        count=1
        ans=""
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                ans+=str(count)
                ans+=s[i]
                count=1
        ans+=str(count)+s[-1]
        print(ans)


if __name__=="__main__":
    solve()