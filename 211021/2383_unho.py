import sys
from collections import deque
sys.stdin = open('input.txt')


def solution(arr, stair_idx):
    down = deque()
    minutes = 0
    idx = 0
    while idx < len(arr) or down:
        # print('---------------- time --------------------')
        # print('----- 시작 전 ------')
        # print(f'흐른 시간 : {minutes}')
        # print(f'사람들 계단까지 남은 시간 : {arr}')
        # print(f'계단에 있는 사람 남은 시간 : {down}')

        minutes += 1
        if len(down):                      # 계단 누구 있을때
            for k in range(len(down)):     # 계단에 있는 사람 시간 경과
                down[k] -= 1

        k = 0
        while k < len(down):
            if down[k] == 0:            # 계단 모두 내려오면
                down.popleft()          # 계단에서 제거
            else:
                k += 1

        for k in range(idx, len(arr)):              # 해당 계단을 가려는 모든 사람들
            if arr[k] <= 0 and len(down) < 3:       # 계단에 도착했고, 3명이 꽉 차지 않았으면 추가
                down.append(stair[stair_idx][2])
                idx += 1
            elif arr[k]:                            # 계단 꽉 찼으면 대기
                arr[k] -= 1

        # print('----- 시작 후 ------')
        # print(f'흐른 시간 : {minutes}')
        # print(f'사람들 계단까지 남은 시간 : {arr}')
        # print(f'계단에 있는 사람 남은 시간 : {down}')

    return minutes
            



T = int(input())
answer = []

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    tc_answer = 1e8

    num = 0                             # 사람 번호
    people = []                         # 사람들 위치 좌표
    stair = []                          # 계단 위치 좌표
    distance = []                       # 각 사람당 계단과의 거리 [0번계단, 1번계단]
    first, second = deque(), deque()    # 각 계단으로 가는 명단(계단까지 남은 시간)

    for i in range(N):                  # 사람들과 계단 위치 찾기
        for j in range(N):
            if board[i][j] == 1:
                people.append([i, j])
            elif board[i][j]:
                stair.append((i, j, board[i][j]))

    for person in people:               # 사람별로 계단과의 거리 구함
        tmp_1 = abs(person[0] - stair[0][0]) + abs(person[1] - stair[0][1])
        tmp_2 = abs(person[0] - stair[1][0]) + abs(person[1] - stair[1][1])
        distance.append((tmp_1, tmp_2))
    

    for i in range(1 << len(people)):   # 누가 어디로 가는지 모든 경우의 수 (2^N)
        first.clear()
        second.clear()

        for j in range(len(people)):
            if i & (1 << j):
                second.append(distance[j][1])       # 계단까지의 거리 저장
            else:
                first.append(distance[j][0])

        first = sorted(first)
        second = sorted(second)

        tmp_time_1 = solution(first, 0)             # 각 계단을 갔을때, 소요되는 총 시간 각자 구하기
        tmp_time_2 = solution(second, 1)

        if tc_answer > max(tmp_time_1, tmp_time_2):     # 각 계단별로 소요된 시간에서, 모든 사람이 다 도착하려면 최대로 긴 시간이 필요하므로 max
            tc_answer = max(tmp_time_1, tmp_time_2)

    answer.append('#{} {}'.format(tc, tc_answer))

print(*answer, sep='\n')