import sys
sys.stdin = open('15900_input.txt')
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(now):
    visited[now] = 1
    for next in tree[now]:
        if not visited[next]:
            dist[next] = dist[now] + 1
            dfs(next)


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

ans = 0
dist = [0] * (N+1)
visited = [0] * (N+1)

dfs(1)

for i in range(2, N+1):
    if len(tree[i]) == 1:
        ans += dist[i]

if ans % 2:
    print("Yes")
else:
    print("No")



# 시간초과
# import sys
# sys.stdin = open('15900_input.txt')
# # input = sys.stdin.readline
# from collections import deque
#
# N = int(input())
# tree = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     x, y = map(int, input().split())
#     tree[x].append(y)
#     tree[y].append(x)
#
# ans = 0
# visited = [0] * (N+1)
#
# q = deque()
# q.append([1, 0])
#
# while q:
#     p, cnt = q.popleft()
#     visited[p] = 1
#     is_leaf = True
#     for i in tree[p]:
#         if not visited[i]:
#             q.append([i, cnt+1])
#             is_leaf = False
#     if is_leaf:
#         ans += cnt
#
# if ans % 2:
#     print("Yes")
# else:
#     print("No")