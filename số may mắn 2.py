def check(n):
    for char in n:
        if char!='4' and char!='7':
            return False

    return True
def solve():
    t=int(input())
    for _ in range(t):
        n=input()
        if check(n):
            print("Yes")
        else:
            print("No")

if __name__== "__main__":
    solve()