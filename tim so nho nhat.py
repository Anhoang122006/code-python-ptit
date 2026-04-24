def solve():
    t = int(input())
    for _ in range(t):
        string = input()
        s_clean = ""
        for char in string:
            if char.isdigit():
                s_clean += char
            else:
                s_clean += " "

        ans = s_clean.split()
        if (len(ans) > 0):
            number = []
            for x in ans:
                number.append(int(x))

            print(min(number))

if __name__=="__main__":
    solve()
    