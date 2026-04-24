T = int(input())

for _ in range(T):
    M, N = map(int, input().split())
    H = [list(map(int, input().split())) for _ in range(M)]

    ans = 0

    for i in range(M):
        for j in range(N):
            if H[i][j] > 0:
                ans += 2  # top + bottom

            # 4 hướng
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy

                if 0 <= ni < M and 0 <= nj < N:
                    ans += max(0, H[i][j] - H[ni][nj])
                else:
                    ans += H[i][j]  # cạnh ngoài

    print(ans)
