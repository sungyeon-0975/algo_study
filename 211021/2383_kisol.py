import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
'''
1 : 사람
2~10 : 계단입구(길이)
'''


def cal_time(stair, p):  # stair: 몇번 계단인지, p: 해당계단을 이용한 사람 배열
    if not p: return 0  # 배열이 비어있으면 0

    time = 0
    Q = p[:3]  # 계단에는 세명까지 오를수 있기때문에 3개까지 가져옴
    p = p[3:]  # 나머지 사람들

    while Q:
        time += 1  # 1분씩 증가시킴
        for i in range(len(p)):  # 계단 위에 먼저 오르지 못한 사람들은 이동거리+대기시간+계단길이에서 대기시간까지만 -1을 해줌
            if p[i][stair - 1] > s[stair - 1][2]:
                p[i][stair - 1] -= 1
        for j in range(len(Q)):  # 계단 위에 먼저 오를사람들은 이동거리+대기시간+계단길이에서 -1씩 계속 해줌
            if Q[j][stair - 1] > 0:
                Q[j][stair - 1] -= 1  # 0보다 큰 경우 -1
        while Q:
            if Q[0][stair - 1] == 0:  # 계단 위에서 전체 시간이 0이되면 다 이동한 것이므로 pop
                Q.pop(0)
                if p:  # 계단 외의 사람들 중에서 제일 가까운 사람을 Q로 가져옴
                    Q.append(p.pop(0))
            else: break

    return time


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())  # 방의 한 변 길 이
    arr = [list(map(int, input().split())) for _ in range(N)]  # 지도
    s = []  # 계단 2개(행, 열, 길이)
    p_pos = []  # 사람 위치(행, 열)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:  # 사람인 경우, 사람 위치 추가
                p_pos.append([i, j])
            elif arr[i][j] > 1:  # 계단인 경우, 계단 위치와 길이 추가
                s.append((i, j, arr[i][j]))

    p = [[0, 0, 0] for _ in range(len(p_pos))]  # 사람 별(1번계단 시간, 2번계단 시간, 1번계단과 2번계단 시간 차이)
    for i in range(len(p)):
        p[i][0] = s[0][2] + abs(p_pos[i][0] - s[0][0]) + abs(p_pos[i][1] - s[0][1]) + 1  # 1번계단까지의 이동시간 + 대기시간(1분) + 계단내려가는 시간
        p[i][1] = s[1][2] + abs(p_pos[i][0] - s[1][0]) + abs(p_pos[i][1] - s[1][1]) + 1  # 2번계단까지의 이동시간 + 대기시간(1분) + 계단내려가는 시간
        p[i][2] = p[i][0] - p[i][1]  # 1번계단과 2번계단의 시간 차이

    p_choose = sorted(p, key=lambda x: x[2])  # 1번계단과 2번계단의 시간 차이 기준으로 정렬 (1번계단이 더 짧은사람 -> 2번계단이 더 짧은 사람)

    if len(p) == 1:  # 사람이 한명이면 2개 계단 중 짧은 시간 출력
        print('#{} {}'.format(tc, min(p_choose[0][0], p_choose[0][1])))
        continue

    temp = [p_choose[r][:] for r in range(len(p_choose))]  # 주소복사 방지를 위해 새로운 2차원 배열 생성
    res = cal_time(2, sorted(temp[:], key=lambda x: x[1]))  # 모든 사람이 다 2번계단을 이용했을 때의 시간 구해줌

    for i in range(1, len(p) + 1):  # 2번보다 1번계단이 더 빠른 사람순으로 한명씩 1번계단을 이용하는사람을 늘리면서 가장 최소시간 구함
        temp = [p_choose[r][:] for r in range(len(p_choose))]
        time = max(cal_time(1, sorted(temp[:i], key=lambda x: x[0])),
                   cal_time(2, sorted(temp[i:], key=lambda x: x[1])))  # 2개 계단 중 더 오래 걸리는 시간이 전체 시간

        if res < time:  # time이 이전보다 커지는 순간이 최소시간 다음임
            break
        elif res > time:  # time이 더 작아지면 res를 time으로 교체
            res = time

    print('#{} {}'.format(tc, res))
