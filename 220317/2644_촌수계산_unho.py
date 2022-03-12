import sys
from collections import deque
sys.stdin = open('input.txt')

def solution():                                     
    q = deque([p1])
    visited[p1] = 0                                 # 본인 촌수는 0부터 시작

    while q:
        node = q.popleft()
        for e in linked[node]:                      # 연결된 다음 노드
            if visited[e] == -1:                    
                visited[e] = visited[node] + 1      # 촌수 증가
                q.append(e)



N = int(sys.stdin.readline())                       # 사람 수
p1, p2 = map(int, sys.stdin.readline().split())     # 촌수 찾으려는 두명
E = int(sys.stdin.readline())                       # 연결 관계 수

visited = [-1] * (N+1)                              # 노드 방문 여부
linked = [[] for _ in range(N+1)]                   # 연결 관계 리스트

for _ in range(E):                                  # 연결 관계 생성
    x, y = map(int, sys.stdin.readline().split())
    linked[x].append(y)
    linked[y].append(x)

solution()

if visited[p2] == -1:           # p2와 연결되어 있지 않으면 -1 반환
    print(-1)
else:
    print(visited[p2])          # 연결되어 있으면 촌수 반환