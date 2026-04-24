def check(s1):
    s2=s1[::-1]
    for i in range(1,len(s1)):
        diff1=abs(ord(s1[i])-ord(s1[i-1]))
        diff2=abs(ord(s2[i])-ord(s2[i-1]))
        if diff1 != diff2:
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

if __name__ == '__main__':
    solve()