import sys
sys.stdin = open('18352_input.txt')
"""
99720KB, 2264ms
"""
input = sys.stdin.readline
from collections import deque
N,M,K,X = map(int,input().split())
def bfs(X):
    queu = deque([X])
    while queu:
        node = queu.popleft()
        for i in graph[node]:
            if answer[i] == -1:
                answer[i] = answer[node] + 1
                queu.append(i)

graph = [[] for _ in range(N+1)]
answer = [-1]*(N+1)
answer[X] = 0

for _ in range(M):
    a,b = list(map(int,input().split()))
    graph[a].append(b)

bfs(X)
print(answer)

for i in range(N+1):
    if answer[i] == K:
        print(i)
if K not in answer:
    print(-1)