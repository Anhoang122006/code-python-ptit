n = int(input())
a = list(map(int, input().split()))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

max_steps = 0

for x in a:
    if is_prime(x):
        continue

    step = 0
    while True:
        step += 1
        if is_prime(x - step) or is_prime(x + step):
            max_steps = max(max_steps, step)
            break

print(max_steps)
