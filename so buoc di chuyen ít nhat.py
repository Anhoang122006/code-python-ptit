import heapq

def solve():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())

        A = [list(map(int, input().split())) for _ in range(n)]

        INF = 10**18
        dist = [[INF]*m for _ in range(n)]

        pq = []
        dist[0][0] = 0
        heapq.heappush(pq, (0, 0, 0))  # (cost, i, j)

        while pq:
            cost, i, j = heapq.heappop(pq)

            if cost > dist[i][j]:
                continue

            # xuống
            if i+1 < n:
                new_cost = cost + abs(A[i][j] - A[i+1][j])
                if new_cost < dist[i+1][j]:
                    dist[i+1][j] = new_cost
                    heapq.heappush(pq, (new_cost, i+1, j))

            # phải
            if j+1 < m:
                new_cost = cost + abs(A[i][j] - A[i][j+1])
                if new_cost < dist[i][j+1]:
                    dist[i][j+1] = new_cost
                    heapq.heappush(pq, (new_cost, i, j+1))

            # chéo
            if i+1 < n and j+1 < m:
                new_cost = cost + abs(A[i][j] - A[i+1][j+1])
                if new_cost < dist[i+1][j+1]:
                    dist[i+1][j+1] = new_cost
                    heapq.heappush(pq, (new_cost, i+1, j+1))

        ans = dist[n-1][m-1]
        print(ans if ans != INF else -1)

solve()
