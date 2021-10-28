"""
Memory - 29 mb
Time - 68 ms

1. 초기 2차원 배열 (0-바다 / 1-섬)
    섬이 어떠한 섬인지 구분을 할 수 없음 -> 섬에 번호를 매겨서 섬을 구분할 필요가 있음 (노드 관계 설정)
    따로 변수를 생성하지 않고, 초기 배열에서 값을 바꿔줌 (섬의 시작 번호는 2번부터 시작, 1번부터 시작시 기존에 값이 1이라 오류 발생)

2. 2차원 배열 순회하며 완전 탐색
    현재 좌표가 섬인 경우, 앞으로 나아감 (DFS 탐색) -> 다른 섬을 발견시 (다리의 길이, 출발한 섬의 번호, 도착 섬 번호) 형식으로 연결 관계를 담아둔 리스트에 쌓음

3. 위에서 구한 연결 관계를 토대로 크루스칼 이용하여 MST 구함
"""


import sys
from pprint import pprint
sys.stdin = open('input.txt')


def find_set(x):
    if x != s[x]:
        s[x] = find_set(s[x])
    return s[x]


def union(x, y):
    s[find_set(y)] = find_set(x)


def kruskal():
    global answer

    idx, edge_cnt = 0, 0

    while edge_cnt != num-3:                # 다리의 개수가 (섬 개수-1)개 일때
        if idx == len(linked):              # 모든섬을 연결할 수 없으면 -1 반환
            answer = -1
            return
        x = linked[idx][1]
        y = linked[idx][2]

        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            answer += linked[idx][0]
        idx += 1


def solution(i, j, d, length, number):                          # 연결관계 찾는 함수 (i,j - 좌표값 / d - 진행방향 / length - 다리 길이 / number - 출발한 섬의 번호)
    if land[i][j] and land[i][j] != number:                     # 현재 좌표가 섬이고, 출발한 섬과 다른 섬일때
        if length > 2:                                          # 다리의 길이가 2 초과일때
            linked.append((length-1, number, land[i][j]))       # 다리의길이, 출발 섬 번호, 도착 섬 번호
        return      

    r = i + dr[d]       # 다음 좌표
    c = j + dc[d]
    
    if 0 <= r < N and 0 <= c < M:       # 범위 안이라면
        if land[r][c] == number:        # 다음 좌표도 같은 섬이라면, 이동 중지
            return
        else:                                       # 다음 좌표가 바다이거나, 다른 섬이면, 재귀 호출
            solution(r, c, d, length+1, number)


def allocate_land(i, j):        # 섬 구분을 위한 DFS 탐색
    stack = [(i, j)]            # 첫 좌표

    while stack:
        node = stack.pop()
        if land[node[0]][node[1]] == 1:         # 현재 위치의 값이 1일때 (섬인데, 아직 섬 번호가 매겨지지 않은 경우)
            land[node[0]][node[1]] = num        # 현재 위치 섬 번호 지정
            for k in range(4):                  # 델타탐색 하며
                r = node[0] + dr[k]
                c = node[1] + dc[k]

                if 0 <= r < N and 0 <= c < M and land[r][c] == 1:       # 현재 위치와 함께 이어진 섬인 경우에 반복
                    stack.append((r, c))


dr = [-1, 0, 1, 0]      # 델타 탐색을 위함
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())                               # 세로, 가로
land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]     # 땅의 정보

linked = []         # 섬들간 연결 관계 담아두는 리스트
answer = 0          # MST 거리


num = 2                             # 섬의 번호, 초기 2차원 배열에 0, 1 이 있으므로 섬의 첫번째 번호는 2번으로 시작하여 구분
for i in range(N):
    for j in range(M):
        if land[i][j] == 1:         # 섬인 경우, DFS 탐색
            allocate_land(i, j)
            num += 1                # 다음 섬 번호를 매기기 위해 값 증가

s = [x for x in range(num)]         # 크루스칼을 위한 집합 생성

# print('섬 번호가 할당 된 이후')
# pprint(land)

for i in range(N):                                      # 2차원 배열 순회
    for j in range(M):                              
        if land[i][j]:                                  # 현재 좌표가 섬이라면
            for d in range(4):                          # 현재 위치에서 상하좌우 탐색
                solution(i, j, d, 0, land[i][j])        # DFS 탐색

linked.sort(key=lambda x: x[0])
# print('섬 간에 연결 관계')
# print(linked)

kruskal()
print(answer)