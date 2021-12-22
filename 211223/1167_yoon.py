import sys
sys.stdin = open('1167_input.txt')
# input = sys.stdin.readline

# 69692KB / 7784ms

def dfs(start, visited):
    for (n, d) in tree[start]:
        if not visited[n]:
            visited[n] = visited[start] + d
            dfs(n, visited)


V = int(input())
tree = [[] for _ in range(V+1)]
mid, answer = 0, 0

for _ in range(V):
    node, *kwargs = map(int, input().split())
    while len(kwargs) > 1:
        tree[node].append((kwargs.pop(0), kwargs.pop(0)))

visited = [0] * (V+1)
dfs(1, visited)
visited[1] = 0
mid = visited.index(max(visited))
visited = [0] * (V+1)
dfs(mid, visited)
visited[mid] = 0

print(max(visited))