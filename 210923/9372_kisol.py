import sys

# 30704KB / 256ms
# input = sys.stdin.readline
sys.stdin = open('input_9372.txt')


def dfs(start):
    global cnt
    visited[start] = 1
    for w in G[start]:
        if not visited[w]:
            cnt += 1
            dfs(w)

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    cnt = 0

    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    dfs(1)
    print(cnt)
