import sys
sys.stdin = open('1167_input.txt')


def dfs(node, distance):                # 노드 번호 / 현재까지 지름
    global longest, start               # 전역 변수 사용 위함

    if distance > longest:              # 지금까지 거리가 가장 긴 지름보다 큰 경우
        longest = distance              # 지름 값 갱신
        start = node                    # 가장 긴 지름의 도착 노드 번호

    for e in linked[node]:              # 현재 노드와 연결된 노드들 순환
        if not visited[e[0]]:           # 아직 방문하지 않은 노드인 경우
            visited[node] = 1           # 방문 처리
            dfs(e[0], distance+e[1])    # 다음 탐색 (재귀)


V = int(sys.stdin.readline())           # 노드의 개수
linked = [[] for _ in range(V+1)]       # 트리의 연결 관계
longest = 0                             # 가장 먼 거리를 저장하는 변수
start = 0                               # 트리 1회 탐색 후 가장 먼 거리에 있는 노드의 번호

for i in range(V):
    value = list(map(int, sys.stdin.readline().split()))    # 입력받은 노드의 연결 관계
    for j in range(1, len(value)-1, 2):                     # 1번 인덱스부터 2개씩, 연결된 노드 번호 / 거리 의 값이 들어와서 그 개수만큼 반복
        linked[value[0]].append((value[j], value[j+1]))     # 튜플 형식으로 (연결된 노드 번호, 노드까지의 거리)

for e in [start, start]:        # 초기 랜덤한 노드에서 탐색 시작 / 초기 탐색에서 찾은 가장 멀리 있는 노드에서 다시 탐색
    visited = [0] * (V+1)       # 방문 리슽트 초기화
    dfs(start, 0)               # 출발 노드 번호 / 현재까지 지름

print(longest)                  # 출력



"""
초기 단순히 노드들마다 가장 먼거리를 찾아서 가장 먼곳을 찾으려 했으나
시간 초과 발생
"""
# def dfs(start):
#     global answer

#     visited = [False] * (V+1)
#     distance = [0] * (V+1)
#     stack = [start]
    
#     while stack:
#         node = stack.pop()
#         if not visited[node]:
#             visited[node] = True
#             for e in linked[node]:
#                 if not visited[e[0]]:
#                     distance[e[0]] = e[1] + distance[node]
#                 stack.append(e[0])
    
#     answer = max(answer, max(distance))


# V = int(sys.stdin.readline())
# linked = [[] for _ in range(V+1)]

# for i in range(V):
#     value = list(map(int, sys.stdin.readline().split()))
#     for j in range(1, len(value)-1, 2):
#         linked[value[0]].append((value[j], value[j+1]))

# answer = 0

# for i in range(1, V+1):
#     dfs(i)

# print(answer)