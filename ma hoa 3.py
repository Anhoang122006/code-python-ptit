def rotate(s):
    total = 0
    for c in s:
        total += ord(c) - ord('A')

    result = ""
    for c in s:
        val = (ord(c) - ord('A') + total) % 26
        result += chr(val + ord('A'))

    return result


def merge(s1, s2):
    result = ""
    for i in range(len(s1)):
        val = (ord(s1[i]) - ord('A') + ord(s2[i]) - ord('A')) % 26
        result += chr(val + ord('A'))

    return result


t = int(input())
for _ in range(t):
    s = input().strip()

    n = len(s)
    half = n // 2

    s1 = s[:half]
    s2 = s[half:]

    r1 = rotate(s1)
    r2 = rotate(s2)

    print(merge(r1, r2))
