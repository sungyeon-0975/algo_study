import sys
import heapq
sys.stdin = open('input.txt')

def solution(start):
    heap = [(0, start)]                     # 시작 거리, 시작 노드

    while heap:
        node = heapq.heappop(heap)
        if not visited[node[1]]:            # 아직 방문하지 않은 학교인 경우
            visited[node[1]] = 1            # 방문 처리
            distance[node[1]] = node[0]     # 최소 거리 저장
            for e in linked[node[1]]:       # 현재 노드에서 다음으로 갈 수 있는 경로 최소힙으로 저장
                heapq.heappush(heap, e)


N, M = map(int, sys.stdin.readline().split())           # 학교의 개수, 도로의 개수
types = [''] + list(sys.stdin.readline().split())       # 학교 종류 리스트

linked = [[] for _ in range(N+1)]                       # 학교들 연결관계
distance = [0] + [1e10] * (N)                           # 학교들간 거리 리스트
visited = [0] * (N+1)                                   # 학교들 방문 여부

for _ in range(M):
    u, v, d = map(int, sys.stdin.readline().split())    # 출발 노드, 도착 노드, 거리
    
    if types[u] != types[v]:            # 서로 다른 종류의 학교인 경우
        linked[u].append((d, v))        # 양방향 저장
        linked[v].append((d, u))

solution(1)                 # 탐색

if sum(visited) == N:       # 모든 학교가 이어진다면 연결된 최소 거리 반환
    print(sum(distance))
else:                       # 모든 학교가 연결되지 않는다면 -1 출력
    print(-1)