from collections import defaultdict

def dfs(u, visited, removed, adj):
    visited[u] = True
    for v in adj[u]:
        if not visited[v] and v != removed:
            dfs(v, visited, removed, adj)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    adj = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    max_comp = -1
    answer = 0

    for removed in range(1, n + 1):
        visited = [False] * (n + 1)
        comp = 0

        for i in range(1, n + 1):
            if i != removed and not visited[i]:
                dfs(i, visited, removed, adj)
                comp += 1

        if comp > max_comp:
            max_comp = comp
            answer = removed

    print(answer if max_comp > 1 else 0)
