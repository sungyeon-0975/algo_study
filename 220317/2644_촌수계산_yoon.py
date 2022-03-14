from collections import deque
import sys
sys.stdin = open('2644_input.txt')
# input = sys.stdin.readline

# 32404KB / 88ms

def bfs(x, y):
    q = deque()
    q.append((x, 0))
    visited = [0] * (n+1)
    visited[x] = 1
    while q:
        s, cnt = q.popleft()
        if s == y:
            return cnt
        for i in range(1, n+1):
            if (parent[i] == s or parent[s] == i) and not visited[i]:
                q.append((i, cnt+1))
                visited[i] = 1


n = int(input())
a, b = map(int, input().split())
m = int(input())
parent = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    parent[y] = x
ans = bfs(a, b)
if not ans:
    ans = -1
print(ans)