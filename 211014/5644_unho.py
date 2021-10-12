"""
Memory - 61,328 kb
Time - 262 ms

문제 푸는데 소요 시간 약 5시간...
끝없는 조건문...
"""


import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(y, x, coverage, num):
    visited = [[0] * 10 for _ in range(10)]

    q = deque([(y, x)])
    visited[y][x] = 1
    board[y][x] += [num]

    while q:
        node = q.popleft()

        for k in range(1, 5):
            r = node[0] + dr[k]
            c = node[1] + dc[k]

            if 0 <= r < 10 and 0 <= c < 10 and not visited[r][c]:
                if visited[node[0]][node[1]] < coverage:
                    visited[r][c]= visited[node[0]][node[1]] + 1
                    board[r][c] += [num]
                    q.append((r, c))



dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    M, A = map(int, input().split())                # 이동 시간 / BC 개수
    board = [[[] for _ in range(10)] for _ in range(10)]            # 충전소 정보가 담긴 2차원 배열
    info = [0] * (A+1)                                              # 충전소별 충전량 정보가 담긴 배열
    sum_charge = 0

    move_A = [0] + list(map(int, input().split()))       # 사용자 이동 정보 (0-이동x, 1-상, 2-우, 3-하, 4-좌)
    move_B = [0] + list(map(int, input().split()))

    for num in range(1, A+1):                       # 위치별 충전소 여부
        x, y, c, p = map(int, input().split())
        info[num] = p
        bfs(y-1, x-1, c+1, num)

    location = [[0, 0], [9, 9]]                     # 사용자별 위치 A / B

    for idx in range(M+1):
        location[0] = [location[0][0] + dr[move_A[idx]], location[0][1] + dc[move_A[idx]]]
        location[1] = [location[1][0] + dr[move_B[idx]], location[1][1] + dc[move_B[idx]]]

        # print(f'충전량 정보 : {info}')

        # for i in range(10):
        #     for j in range(10):
        #         if i == location[0][0] and j == location[0][1]:
        #             print('\033[32m', board[i][j], end=' ')
        #         elif i ==location[1][0] and j == location[1][1]:
        #             print('\033[31m', board[i][j], end=' ')
        #         else:
        #             print(board[i][j], end=' ')
        #     print()

        # print(f'A 위치 : {location[0]} / B 위치 : {location[1]}')

        if board[location[0][0]][location[0][1]]:                                                       # A 가 충전소 안에 있을때

            if len(board[location[0][0]][location[0][1]]) == 1:                                         # A 가 충전소 하나인곳에 있을때
                if board[location[0][0]][location[0][1]][0] in board[location[1][0]][location[1][1]]:   # b도 같은 충전소에 있을때
                    if len(board[location[1][0]][location[1][1]]) == 1:                                 # 이 충전소가 유일하면
                        sum_charge += info[board[location[0][0]][location[0][1]][0]]                    # A와 B 둘다 충전소가 하나로 동일하여 그냥 충전소 하나꺼만 충전
                    elif len(board[location[1][0]][location[1][1]]) > 1:                                # b 는 여러개일때
                        tmp = set(board[location[1][0]][location[1][1]]).difference(board[location[0][0]][location[0][1]])
                        tmp_max = 0
                        for e in tmp:
                            if tmp_max < info[e]:
                                tmp_max = info[e]
                        sum_charge += info[board[location[0][0]][location[0][1]][0]] + tmp_max

                else:                                                                                   # B랑 서로 같은 충전소 아닐때
                    if len(board[location[1][0]][location[1][1]]) == 1:                                 # B도 하나라면
                        sum_charge += info[board[location[0][0]][location[0][1]][0]] + info[board[location[1][0]][location[1][1]][0]]     # A랑 B 따로 충전
                    elif not board[location[1][0]][location[1][1]]:                                     # b 하나도 없을때
                        sum_charge += info[board[location[0][0]][location[0][1]][0]]
                    else:                                                                               # B 여러개일때
                        tmp_max = 0
                        for e in board[location[1][0]][location[1][1]]:
                            if tmp_max < info[e]:
                                tmp_max = info[e]
                        sum_charge += info[board[location[0][0]][location[0][1]][0]] + tmp_max

            else:                                                                                       # A 충전소가 여러개 있을때

                if len(board[location[1][0]][location[1][1]]) == 1:                                     # B 충전소 하나일때

                    if board[location[1][0]][location[1][1]][0] in board[location[0][0]][location[0][1]]:   # 충전소 겹칠때
                        tmp = set(board[location[0][0]][location[0][1]]).difference(board[location[1][0]][location[1][1]])
                        tmp_max = 0
                        for e in tmp:
                            if tmp_max < info[e]:
                                tmp_max = info[e]
                        sum_charge += info[board[location[1][0]][location[1][1]][0]] + tmp_max
                    else:                                                                               # 충전소 안겹치면
                        tmp_max = 0
                        for e in board[location[0][0]][location[0][1]]:
                            if tmp_max < info[e]:
                                tmp_max = info[e]
                        sum_charge += info[board[location[1][0]][location[1][1]][0]] + tmp_max

                elif len(board[location[1][0]][location[1][1]]) > 1:                       # B 충전소 여러개일때
                    tmp_max = 0
                    for e1 in board[location[0][0]][location[0][1]]:
                        for e2 in board[location[1][0]][location[1][1]]:
                            if e1 != e2 and tmp_max < (info[e1] + info[e2]):
                                tmp_max = info[e1] + info[e2]
                    sum_charge += tmp_max
                
                elif not board[location[1][0]][location[1][1]]:
                    tmp_max = 0
                    for e in board[location[0][0]][location[0][1]]:
                        if tmp_max < info[e]:
                            tmp_max = info[e]
                    sum_charge += tmp_max
                                
            
        elif board[location[1][0]][location[1][1]]:         # B 충전소 안에 있을때
            if len(board[location[1][0]][location[1][1]]) == 1:     # b - 1
                sum_charge += info[board[location[1][0]][location[1][1]][0]]
            else:                                           # b - many
                tmp_max = 0
                for e in board[location[1][0]][location[1][1]]:
                    if tmp_max < info[e]:
                        tmp_max = info[e]
                sum_charge += tmp_max
        

        # print(f'{idx}초 - 충전량 {sum_charge}')

    answer.append('#{} {}'.format(tc, sum_charge))

print(*answer, sep='\n')


""" import sys
from collections import deque
import os
import time
from pprint import pprint
sys.stdin = open('input.txt')


def bfs(y, x, coverage, performace, num):      # 좌표 / 남은 충전 범위 / 충전 성능 / BC 이름
    visited = [[0] * 10 for _ in range(10)]

    q = deque([(y, x)])
    board[y][x] += [(num, performace)]          # 해당 좌표에 어떤 BC 이고, 성능인지 튜플로 담김
    visited[y][x] = 1

    while q:
        node = q.popleft()

        for k in range(1, 5):
    
            r = node[0] + dr[k]
            c = node[1] + dc[k]

            if 0 <= r < 10 and 0 <= c < 10 and not visited[r][c]:       
                if visited[node[0]][node[1]] == coverage:               # 설정된 영영에 도착하면 종료
                    return

                visited[r][c] = visited[node[0]][node[1]] + 1
                board[r][c] += [(num, performace)]
                q.append((r, c))


dr = [0, -1, 0, 1, 0]       # 이동 - 이동하지 않음 / 상 / 우 / 하 / 좌 
dc = [0, 0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    M, A = map(int, input().split())        # 이동 시간 / BC 개수
    board = [[[] for _ in range(10)] for _ in range(10)]

    move_A = tuple(map(int, input().split()))       # 사용자 이동 정보 (0-이동x, 1-상, 2-우, 3-하, 4-좌)
    move_B = tuple(map(int, input().split()))

    location_A = [0, 0]                 # 사용자별 위치
    location_B = [9, 9]

    charge_A = board[0][0]              # 사용자별 충전량 (초기 위치에서 충전 상태)
    charge_B = board[9][9]

    for idx in range(1, A+1):
        x, y, C, P = map(int, input().split())      # BC 좌표 / 충전 범위 / 충전량
        bfs(y-1, x-1, C+1, P, idx)                  # 충전 정보 저장

    for i in range(10):
        for j in range(10):
            print(board[i][j], end=' ')
        print()

    for idx in range(M):
        location_A[0] = location_A[0] + dr[move_A[idx]]
        location_A[1] = location_A[1] + dc[move_A[idx]]

        location_B[0] = location_B[0] + dr[move_B[idx]]
        location_B[1] = location_B[1] + dc[move_B[idx]]

        sign = False
        duplicate = []
        for e in board[location_A[0]][location_A[1]]:
            if e in board[location_B[0]][location_B[1]]:
                duplicate.append()
                sign = True
        
        if not sign:
            charge_A = sorted(board[location_A[0]][location_A[1]], key=lambda x: (x[1]))[-1]
            charge_B = sorted(board[location_B[0]][location_B[1]], key=lambda x: (x[1]))[-1]
        # elif sign:
 """