import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def check(s):
    prime_digits={'2', '3', '5', '7'}
    for i in range(len(s)):
        index_digit=is_prime(i)
        char_is_prime=s[i] in prime_digits
        if index_digit != char_is_prime:
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
