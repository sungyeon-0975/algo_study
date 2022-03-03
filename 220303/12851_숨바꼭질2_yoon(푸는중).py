import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
sec, cnt = 10e2, 0
q = deque([N])
visited[N] = 1
while q:
    now = q.popleft()
    if visited[now] > sec:
        break
    if now == K:
        sec = visited[now]
        cnt += 1
    for next in [now-1, now+1, now*2]:
        if 0 <= next <= 100000:
            if not visited[next] or visited[next] == visited[now] + 1:
                visited[next] = visited[now]+1
                q.append(next)
print(sec-1)
print(cnt)