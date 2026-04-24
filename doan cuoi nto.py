import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def check(s):
    m=int(s[-4:])
    if not is_prime(m):
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

if __name__ == "__main__":
    solve()
