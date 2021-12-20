import heapq

def dijkstra(start, linked, n):                                     # 다익스트라, 시작 노드 / 연결 관계 리스트 / 노드의 개수
    visited = [0] * (n+1)                                           # 노드 방문 여부 리스트
    distance = [0] * (n+1)                                          # 시작 노드로부터 각 노드까지의 거리 리스트
    heap = [(0, start)]                                             # 최소힙 (거리, 시작 노드)

    while heap:                                                     
        node = heapq.heappop(heap)                                  # 최소힙에서 다음 이동 가능한 노드 정보 꺼냄
        if not visited[node[1]]:                                    # 아직 방문하지 않은 곳 일때
            visited[node[1]] = 1                                    # 방문 처리
            distance[node[1]] = node[0]                             # 해당 노드까지 거리 입력
            for e in linked[node[1]]:                               # 현재 노드와 연결된 다음 노드의 정보들
                heapq.heappush(heap, (1 + distance[node[1]], e))    # 거리를 1 추가하고 힙에 추가
    
    return distance                                                 # 노드의 거리 정보가 담긴 리스트 반환


def solution(n, edges):
    linked = [[] for _ in range(n+1)]                               # 연결 관계 리스트

    for edge in edges:                                              # 노드간 양방향 간선
        linked[edge[0]].append(edge[1])             
        linked[edge[1]].append(edge[0])
    
    distance = dijkstra(1, linked, n)                               # 최초 1회 임의의 노드에서 출발하여 가장 멀리 있는 노드를 구함
    distance = dijkstra(distance.index(max(distance)), linked, n)   # 가장 멀리 있는 노드에서 시작하여 노드의 거리를 구함

    if distance.count(max(distance)) >= 2:                          # 가장 멀리 있는 노드가 두개 이상인 경우
        return max(distance)                                        # 트리의 지름이 중간값이 되므로 트리의 지름 반환

    distance = dijkstra(distance.index(max(distance)), linked, n)   # 가장 멀리 있는 노드가 하나인 경우, 확인을 위해 가장 먼 노드에서 다시 다익스트라 실행

    if distance.count(max(distance)) >= 2:                          # 가장 멀리 있는 노드가 두개라면 트리의 지름 반환
        return max(distance)
    else:                                                           # 가장 멀리 있는 노드가 한개라면, 트리의 지름 -1 반환
        return max(distance) - 1



"""
시간 초과 발생
"""
# import heapq
# from itertools import combinations


# def dijkstra(start, distance, linked, n):
#     visited = [0] * (n+1)
#     heap = [(0, start)]

#     while heap:
#         node = heapq.heappop(heap)
#         if not visited[node[1]]:
#             visited[node[1]] = 1
#             distance[start][node[1]] = node[0]
#             for e in linked[node[1]]:
#                 heapq.heappush(heap, (1+node[0], e))



# def solution(n, edges):
#     distance = [[0] * (n+1) for _ in range(n+1)]
#     linked = [[] for _ in range(n+1)]
#     answer = []

#     for edge in edges:
#         linked[edge[0]].append(edge[1])
#         linked[edge[1]].append(edge[0])
    

#     for i in range(1, n+1):
#         dijkstra(i, distance, linked, n)

#     lst_comb = combinations(range(1, n+1), 3)
    
#     for e in lst_comb:
#         tmp = [0, 0, 0]
#         tmp[0] = distance[e[0]][e[1]]
#         tmp[1] = distance[e[0]][e[2]]
#         tmp[2] = distance[e[1]][e[2]]

#         answer.append(sum(tmp) - max(tmp) - min(tmp))
        
#     return max(answer)


print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(5, [[1,5],[2,5],[3,5],[4,5]]))