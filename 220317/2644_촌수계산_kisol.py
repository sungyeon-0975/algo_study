import sys
from collections import deque

# KB / 88ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_2644.txt')


def bfs():
    global res

    Q = deque()
    Q.append(A)
    visited[A] = 1

    while Q:
        node = Q.popleft()
        for i in tree[node]:
            if not visited[i]:
                if i == B:
                    res = visited[node]
                    return
                visited[i] = visited[node] + 1
                Q.append(i)

T = int(input())

for _ in range(T):
    n = int(input())
    A, B = map(int, input().split())
    m = int(input())
    tree = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for _ in range(m):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)
    res = -1
    bfs()

    print(res)