import sys
import heapq
sys.stdin = open('input.txt')


"""
Python
    Memory - 62 MB
    Time - 0.872 s
"""
def dijkstra(start):                                # 출발 마을 번호
    heap = [(0, start)]                             # (거리, 도착 마을 번호) 

    while heap and distance[start][X] == 0:         # 특정 마을에서 X 마을로 가는 거리만 구하면 되므로 X 마을의 거리값이 계산이 되면 종료
        node = heapq.heappop(heap)                  
        if not visited[start][node[1]]:             # 출발지에서 도착지로 가는곳이 방문하지 않았다면
            visited[start][node[1]] = 1             # 방문처리
            distance[start][node[1]] = node[0]      # 거리값 저장
            for weight, end in linked[node[1]]:     # 도착지에서 다음 도착지로 갈수있는곳만큼 반복
                heapq.heappush(heap, (weight + node[0], end))       # (현재까지 온 거리 + 다음 도착지까지 거리), 도착지


N, M, X = map(int, sys.stdin.readline().split())        # 마을 번호 / 도로 개수 / 도착지

linked = [[] for _ in range(N+1)]                       # 입력되는 도로 연결 관계
visited = [[0] * (N+1) for _ in range(N+1)]             # 2차원 배열의 방문 여부 -> 예) [1][5] -> 1번 마을에서 5번 마을로 가는거 방문 체크 여부
distance = [[0] * (N+1) for _ in range(N+1)]            # 2차원 배열의 최소 거리 저장 변수 -> 예) [2][4] -> 2번 마을에서 4번 마을로 가는 최소 거리
answer = [0] * (N+1)                                    # 각 도시의 도착지 왕복 거리 저장 변수

for _ in range(M):                                                  # 도로 연결 관계 입력 받음
    start, end, weight = map(int, sys.stdin.readline().split())
    linked[start].append((weight, end))

for i in range(1, N+1):         # 다익스트라를 N번 반복 (모든 마을에서 특정 마을로 가는 최소 거리를 구해야 함)
    dijkstra(i)

for i in range(1, N+1):                             # 최소 거리 구함
    answer[i] = distance[i][X] + distance[X][i]     # (i -> X) + (X -> i) 이동 거리 구함

print(max(answer))