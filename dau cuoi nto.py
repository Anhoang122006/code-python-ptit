import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def solve():
    t=int(input())
    for _ in range(t):
        s=input()
        n=s[-3:]
        m=s[:3]
        if is_prime(int(n)) and is_prime(int(m)):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
