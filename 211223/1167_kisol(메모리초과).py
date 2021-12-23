import sys

# KB / ms Python3
# input = sys.stdin.readline
'''
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것
'''

sys.stdin = open('input_1167.txt')


def dfs(node, d):
    global max_d
    if max_d < d:
        max_d = d

    for idx, distance in tree[node]:
        if not visited[node][idx]:
            visited[node][idx] = 1
            visited[idx][node] = 1
            dfs(idx, d + distance)


V = int(input())
arrs = [list(map(int, input().split())) for _ in range(V)]
tree = [[] for _ in range(V + 1)]
visited = [[0] * (V + 1) for _ in range(V + 1)]
max_d = 0

# 트리 만들기
for arr in arrs:
    idx = 1
    node = arr[0]
    while arr[idx] != -1:
        tree[node].append((arr[idx], arr[idx + 1]))
        idx += 2

for i in range(1, V + 1):
    dfs(i, 0)

print(max_d)

# 메모리 초과

# def dfs(node, d):
#     global max_d
#     if max_d < d:
#         max_d = d
#
#     for i in range(1, V + 1):
#         if tree[node][i] and not visited[node][i]:
#             visited[node][i] = 1
#             visited[i][node] = 1
#             dfs(i, d + tree[node][i])
#
#
# V = int(input())
# arrs = [list(map(int, input().split())) for _ in range(V)]
# tree = [[0] * (V + 1) for _ in range(V + 1)]
# visited = [[0] * (V + 1) for _ in range(V + 1)]
# max_d = 0
#
# # 트리 만들기
# for arr in arrs:
#     idx = 1
#     node = arr[0]
#     while arr[idx] != -1:
#         tree[node][arr[idx]] = arr[idx + 1]
#         idx += 2
#
# for i in range(1, V + 1):
#     dfs(i, 0)