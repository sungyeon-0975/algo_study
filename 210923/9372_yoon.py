import sys
# input = sys.stdin.readline
sys.stdin = open('input_9372.txt')

def bfs(s):
    cnt = 0
    q = [s]
    visited[s] = 1
    while q:
        n = q.pop(0)
        for v in graph[n]:
            if visited[v] == 0:
                visited[v] = 1
                q.append(v)
                cnt += 1
    return cnt


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    ans = 0

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N+1):
        if visited[i] == 0:
            ans += bfs(i)

    print(ans)