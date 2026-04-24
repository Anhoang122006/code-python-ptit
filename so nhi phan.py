def solve():

    try:
        n = int(input())
    except EOFError:
        return


    a = list(map(int, input().split()))

    dem = 0


    for i in range(n - 1):
        if a[i] != a[i + 1]:
            dem += 1

    # Bước 4: In kết quả
    print(dem)

if __name__ == "__main__":
    solve()
