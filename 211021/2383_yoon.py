import sys
sys.stdin = open('2383_input.txt')

# 64116KB / 317ms

def down(on_stair, stair_num):                      # (stair에 올라와있는 사람, 1번 or 2번)
    sec, wait = 0, 0                                # 시간, 대기자 수
    now = []                                        # 지금 내려가는 사람 (최대 3명)
    while on_stair or wait or now:
        while wait:                                 # 대기자 있으면
            if len(now) == 3:                       # 내려가는 사람 이미 3명이면 아무것도 할 수 없음
                break
            now.append(stair_num[2])                # 빈 자리 나면 내려가는 목록에 추가(내려가는 데 걸리는 시간)
            wait -= 1                               # 대기자 -1
        for i in range(len(on_stair)-1, -1, -1):    # stair까지 가는 데 걸리는 시간
            on_stair[i] -= 1                        # 1초 지날 때마다 -1
            if on_stair[i] <= 0:                    # 도착했으면 일단 대기목록에 추가
                on_stair.pop(i)
                wait += 1
        for i in range(len(now)-1, -1, -1):         # pop을 위해 거꾸로 - 내려가는 사람 목록
            now[i] -= 1                             # 1초 지날 때마다 -1
            if now[i] <= 0:                         # 다 내려왔으면 목록에서 삭제
                now.pop(i)
        sec += 1                                    # 한 사이클 끝날 때마다 시간 +1
    return sec

def dfs(idx):
    global time
    if idx == len(people):
        stair1, stair2 = [], []
        for i in range(len(people)): # 각 사람이 올라가게 될 stair에 따라 리스트에 거리 넣기
            if visited[i] == 1:
                stair1.append(dist1[i])
            elif visited[i] == 2:
                stair2.append(dist2[i])
        temp = max(down(stair1, stair[0]), down(stair2, stair[1]))
        time = min(time, temp + 1) # 대기시간 1분 포함
        return
    visited[idx] = 1
    dfs(idx+1)
    visited[idx] = 2
    dfs(idx+1)
    visited[idx] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people, stair = [], []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                if arr[i][j] == 1:
                    people.append((i, j)) # (i, j)
                else:
                    stair.append((i, j, arr[i][j])) # (i, j, 높이)

    dist1, dist2 = [0] * len(people), [0] * len(people)

    for idx in range(len(people)):
        pi, pj = people[idx]
        dist1[idx] = abs(pi - stair[0][0]) + abs(pj - stair[0][1])
        dist2[idx] = abs(pi - stair[1][0]) + abs(pj - stair[1][1])

    visited = [0] * len(people) # 어느 stair 탈 건지 표시
    time = 987654321
    dfs(0)

    print('#{} {}'.format(t, time))

    # ----------------------------------------------------------------------
    # if temp >= time:
    #     return
    # if idx == len(people):
    #     if temp < time:
    #         time = temp
    #     return
    # if not visited[idx]:
    #     if visited.count(1) < 3:
    #         visited[idx] = 1
    #         dfs(idx+1, max(temp, dist1[idx] + stair[0][2] + 1))
    #         visited[idx] = 0
    #         if visited.count(2) < 3:
    #             visited[idx] = 2
    #             dfs(idx+1, max(temp, dist2[idx] + stair[1][2] + 1))
    #             visited[idx] = 0
    #     elif visited.count(2) < 3:
    #         visited[idx] = 2
    #         dfs(idx + 1, max(temp, dist2[idx] + stair[1][2] + 1))
    #         visited[idx] = 0
    #     else: # 망했다 대기인원 까먹었다