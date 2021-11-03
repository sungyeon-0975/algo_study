import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')


"""
다익스트라 활용
Python
    Memory - 115 mb
    Time - 3.556 s
"""
def dijkstra():
    heap = [(0, X)]

    while heap:
        node = heapq.heappop(heap)
        if not visited[node[1]]:
            visited[node[1]] = 1
            distance[node[1]] = node[0]
            for e in linked[node[1]]:
                if not visited[e]:
                    heapq.heappush(heap, (distance[node[1]]+1, e))


N, M, K, X = map(int, sys.stdin.readline().split())     # 도시의 개수 / 도로의 개수 / 거리 정보 / 출발 도시 번호

linked = [[] for _ in range(N+1)]   # 도시간 연결 관계
visited = [0] * (N+1)               # 도시 방문 여부
distance = [0] + [1e10] * (N)       # 출발 도시에서 해당 도시와의 최소 거리
distance[X] = 0                     # 출발 도시 시작 거리 0으로 초기화

for _ in range(M):                                      # 연결관계 초기화
    a, b = map(int, sys.stdin.readline().split())
    linked[a].append(b)

dijkstra()

if distance.count(K):
    for i in range(1, len(distance)):
        if distance[i] == K:
            print(i)
else:
    print(-1)



"""
단순 BFS 활용한 풀이
python
    Memory - 113 mb
    Time - 3.33 s
pypy3
    Memory - 235 mb
    Time - 1.58 s
"""

# def bfs():
#     q = deque([X])          # 출발점 추가 및 방문 처리   
#     visited[X] = 1

#     while q:
#         node = q.popleft()
#         for e in linked.get(node, []):
#             if visited[node] == K+1:        # 찾아야 하는 거리만큼의 도시들을 모두 탐색하고 나면 종료
#                 return
#             if not visited[e]:                      # 아직 방문하지 않은 도시이면
#                 visited[e] = visited[node] + 1      # 새로 방문 처리
#                 q.append(e)


# N, M, K, X = map(int, sys.stdin.readline().split())      # 도시 개수 / 도로 개수 / 거리 정보 / 출발 도시
# linked = {}
# visited = [0] * (N+1)

# for _ in range(M):                                  # 연결 관계 설정
#     a, b = map(int, sys.stdin.readline().split())
#     linked[a] = linked.get(a, []) + [b]

# bfs()

# chk = set(visited)      # 시간 단축을 위한 집합화

# if K+1 not in chk:      # 해당 거리만큼의 도시가 없으면 -1 출력
#     print(-1)
# else:                                   # 해당 거리만큼의 도시가 있으면 도시들 출력
#     for i in range(len(visited)):
#         if visited[i] == K+1:
#             print(i)