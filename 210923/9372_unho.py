"""
Memory - 32412 KB (31.65 MB)
Time - 756 ms
"""
import sys
from collections import deque
sys.stdin = open('input_9372.txt')


def BFS(start):
    q = deque([start])
    cnt = 1
    visited[q[0]] = cnt

    while q:
        node = q.popleft()
        for e in link.get(node):
            if not visited[e]:
                cnt += 1
                visited[e] = cnt
                q.append(e)


T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    link = {}
    visited = [0] * (N+1)

    for idx in range(M):
        a, b = map(int, sys.stdin.readline().split())

        link[a] = link.get(a, []) + [b]
        link[b] = link.get(b, []) + [a]


    BFS(1)

    print(max(visited) - 1)