"""
Memory - 64,508 kb
Time - 1,040 ms
"""


import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')


def dfs(y, x, k, rotate):       # 현재 좌표 / 진행 방향 / 방향 전환 횟수
    global max_dessert

    if rotate > 4:              # 4번 회전을 넘으면 종료 / 초과시 사각형이 아님
        return
    
    r = y + dr[k]               # 다음 좌표
    c = x + dc[k]

    # print(f'현재 좌표 : {y}, {x} 방향 : {k}')
    # print(f'디저트 종류 : ', end=' ')
    # for a in range(101):
    #     if case_dessert[a]:
    #         print(a, end=' ')
    # print()

    if 0 <= r < N and 0 <= c < N and not case_dessert[cafe[r][c]]:      # 범위 안이고, 다음 방문할곳 디저트가 새로운 디저트라면
        case_dessert[cafe[r][c]] = 1                                    # 다음 위치 디저트 먹은걸로 체크
        dfs(r, c, k, rotate)                                            # 1번 경우 - 진행 방향 그대로 유지
        dfs(r, c, (k+1)%4, rotate+1)                                    # 2번 경우 - 오른쪽으로 90도 회전하여 진행
        case_dessert[cafe[r][c]] = 0                                    # 다음 위치에서 탐색 끝났으므로, 다음 위치 디저트 삭제
    
    elif r == i and c == j:                                                 # 시작 위치로 돌아오면
        if sum(case_dessert) > 1 and sum(case_dessert) > max_dessert:       # 지금까지 먹은 디저트 개수 확인하여 최고 개수와 비교
            max_dessert = sum(case_dessert)
            # print(f'최고 개수 : {max_dessert} / 시작 위치 : {i}, {j}')
        return

    elif r < 0 and c < 0:           # 각 사각형의 모서리 끝으로 도달시 더 진행 방법이 없으므로 종료
        return
    elif r < 0 and c >= N:
        return
    elif r >= N and c < 0:
        return
    elif r >= N and c >= 0:
        return


dr = [-1, 1, 1, -1]     # 우상 / 우하 / 좌하 / 좌상
dc = [1, 1, -1, -1] 

T = int(input())
answer = []

for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    max_dessert = -1

    for i in range(N):
        for j in range(N):
            case_dessert = [0] * 101            # 디저트 종류 최대 100개 (1 ~ 100)
            case_dessert[cafe[i][j]] = 1        # 시작 위치 디저트 체크
            dfs(i, j, 0, 0)                     # 시작 위치 좌표 / 진행 방향 / 회전한 횟수
                                                # 우상의 경우만 탐색 (어차피 다른 좌표에서 우상으로 시작하면 모두 탐색하게 됨 - 시계 방향으로 탐색하므로)

    answer.append('#{} {}'.format(tc, max_dessert))

print(*answer, sep='\n')