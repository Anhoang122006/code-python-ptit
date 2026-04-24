def check(s):
    for char in s:
        if char not in "012":
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