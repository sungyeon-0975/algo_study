# https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
# 188ms, 29200KB
# tc = int(input())
# for _ in range(tc):
#     N, M = map(int, input().split())
#     for _ in range(M):
#         a, b = map(int, input().split())
#     print(N - 1)

import sys
from collections import deque
input = sys.stdin.readline
# 292ms, 32412KB
# def BFS(idx, cnt):
#     q = deque()
#     q.append(idx)
#     visited[idx] = 1

#     while q:
#         n = q.popleft()
#         for x in tree[n]:
#             if visited[x] == 0:
#                 visited[x] = 1
#                 cnt += 1
#                 q.append(x)
#     return cnt

# tc = int(input())
# for _ in range(tc):
#     N, M = map(int, input().split())
#     tree = [[] for _ in range(N + 1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         tree[a].append(b)
#         tree[b].append(a)
    
#     visited = [0] * (N + 1)
#     print(BFS(1, 0))


# 260ms, 30704KB
def DFS(idx, cnt):
    visited[idx] = 1

    for i in tree[idx]:
        if visited[i] == 0:
            visited[i] = 1
            cnt = DFS(i, cnt + 1)
    return cnt

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    visited = [0] * (N + 1)
    print(DFS(1, 0))