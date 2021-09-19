"""
Memory - 53692 KB (52.43 MB)
Time - 692 ms
"""

import sys
from collections import deque
sys.stdin = open('input_11725.txt')


def BFS(start):
    q = deque([start])
    visited[q[0]] = True

    while q:
        node = q.popleft()
        for e in link.get(node):
            if not visited[e]:
                visited[e] = True
                answer[e-2] = node
                q.append(e)

    

N = int(sys.stdin.readline())
link = {}
visited = [False] * (N+1)
answer = [0] * (N-1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())

    link[a] = link.get(a, []) + [b]
    link[b] = link.get(b, []) + [a]

BFS(1)

for e in answer:
    print(e)