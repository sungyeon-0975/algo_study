from collections import deque
import sys
sys.stdin = open('1963_input.txt')
# input = sys.stdin.readline


def bfs():
    global res
    q = deque()
    q.append([A, 0])
    visited = [0] * 10000
    visited[A] = 1
    while q:
        num, cnt = q.popleft()
        if num == B:
            res = cnt
        if num < 1000:
            continue
        for digit in [1, 10, 100, 1000]:
            base = num - ((num % (digit * 10) // digit) * digit)
            for i in range(10):
                new = base + (i * digit)
                if not visited[new] and prime[new]:
                    visited[new] = 1
                    q.append([new, cnt+1])


prime = [True] * 10000
for i in range(2, 101):
    for j in range(2, 10000//i):
        prime[i*j] = False

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    res = 'Impossible'
    bfs()
    print(res)
