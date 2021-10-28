import sys
sys.stdin = open('5650_input.txt')


BLOCK = {                   # 블럭의 종류별 반사되는 방향
    1: [2, 3, 1, 0],        # 각 0,1,2,3 진행방향으로 접근시 튕겨져 나가는 방향
    2: [1, 3, 0, 2],        # 2번 블록의 경우 0번 방향으로 진행하여 오면 1번 방향으로 튕겨나감
    3: [3, 2, 0, 1],
    4: [2, 0, 3, 1],
    5: [2, 3, 0, 1],
}
 
dr = [-1, 0, 1, 0]          # 델타 탐색 / 위 오른 아래 왼
dc = [0, 1, 0, -1]    
 
T = int(input())
answer = []
 
for tc in range(1, 1+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    warm_hole = [[] for _ in range(5)]          # 웜홀 짝의 좌표가 담길 0번 인덱스 6번 웜홀, 1번 인덱스 7번 웜홀
    link = {}                                   # 같은 번호의 웜홀끼리 좌표값:좌표값 형태로 저장
    tc_answer = 0                               # 정답 변수
 
    for i in range(N):                                      # 2차원 배열을 순회하여 웜홀을 발견하면
        for j in range(N):                                  # 각 번호의 리스트에 웜홀의 좌표값을 저장함
            if board[i][j] > 5:
                warm_hole[board[i][j]-6].append((i, j))

    # for i in range(5):
    #     print(f'{i+6} 번호의 웜홀 좌표 값들 : {warm_hole[i]}')

    for e in warm_hole:             # 웜홀의 좌표:좌표
        if e:
            link[e[0]] = e[1]
            link[e[1]] = e[0]
            # print(f'같은 짝을 가진 웜홀 : {e[0]}:{link[e[0]]} , {e[1]}:{link[e[1]]}')
             
    for i in range(N):                      # 2차원 배열 순회
        for j in range(N):
            if not board[i][j]:             # 현재 위치가 공이 놓일수 있는 위치 (블럭, 블랙홀, 웜홀 아닌 경우)
                for k in range(4):          # 4가지 방향으로 공이 진행
                    cnt = 0                 # 공이 부딪히는 개수 카운트 변수
                    y, x = i, j             # 초기 시작점 셋팅
                    while True:             # 게임이 끝날때까지 반복
                        r = y + dr[k]       # 새로 이동하려는 좌표
                        c = x + dc[k]
 
                        if r == i and c == j:          # 원래 위치로 돌아오면 종료 
                            break
                        
                        y, x = r, c         # 다음 반복에서 사용될 기준 좌표 설정
                        if 0 <= r < N and 0 <= c < N:       # 범위 안일때
                            if 1 <= board[r][c] <= 5:       # 블럭이면
                                cnt += 1                    # 부딪히는 횟수 증가
                                k = BLOCK[board[r][c]][k]   # 블럭에 부딪혀서 진행 방향 변화

                            elif 6 <= board[r][c]:          # 웜홀일 경우
                                y, x = link[(r, c)]         # 다른 웜홀로 이동

                            elif board[r][c] == -1:         # 블랙홀인 경우 종료
                                break

                        else:                           # 범위를 벗어날때 (벽에 부딪히면 횟수 +1, 방향 반대로)
                            cnt += 1    
                            k = (k+2)%4

                    if tc_answer < cnt:     # 부딪힌 횟수가 이전 경우보다 많은 경우 갱신
                        tc_answer = cnt
     
    answer.append('#{} {}'.format(tc, tc_answer))
print(*answer, sep='\n')



""" 재귀로 인한 런타임 에러?? """
# def dfs(y, x, d, cnt):
#     global tc_answer
    
#     r = y + dr[d]
#     c = x + dc[d]

#     if r == i and c == j:          # 원래 위치로 돌아오면
#         if tc_answer < cnt:
#             tc_answer = cnt
#         return

#     if 0 <= r < N and 0 <= c < N:   # 범위 안일때
#         if 1 <= board[r][c] <= 5:
#             dfs(r, c, BLOCK[board[r][c]][d], cnt+1)
#         elif 6 <= board[r][c]:
#             nr, nc = link[(r, c)]
#             dfs(nr, nc, d, cnt)
#         elif board[r][c] == -1:
#             if tc_answer < cnt:
#                 tc_answer = cnt
#             return
#         else:
#             dfs(r, c, d, cnt)
#     else:                           # 범위를 벗어날때 (벽에 부딪히면 횟수 +1, 방향 반대로)
#         dfs(r, c, (d+2)%4, cnt+1)


# BLOCK = {
#     1: [2, 3, 1, 0],
#     2: [1, 3, 0, 2],
#     3: [3, 2, 0, 1],
#     4: [2, 0, 3, 1],
#     5: [2, 3, 0, 1],
# }

# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

# T = int(input())
# answer = []

# for tc in range(1, T+1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     warm_hole = [[] for _ in range(5)]
#     link = {}
#     tc_answer = 0

#     for i in range(N):
#         for j in range(N):
#             if board[i][j] > 5:
#                 warm_hole[board[i][j]-6].append((i, j))
                
#     for e in warm_hole:
#         if e:
#             link[e[0]] = e[1]
#             link[e[1]] = e[0]
            
#     for i in range(N):
#         for j in range(N):
#             if not board[i][j]:
#                 for k in range(4):
#                     dfs(i, j, k, 0)
    
#     answer.append('#{} {}'.format(tc, tc_answer))
# print(*answer, sep='\n')