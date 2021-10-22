import sys

sys.stdin = open('2383_input.txt')
"""
완전탐색
계단마다 걸리는 시간 계산
넣는 스택을 한정하면 되려나
50/49통과 왜...대체 왜....
이미 코드도 많이 수정 본 상태. 그냥 나중에 dfs  로 다시짜는걸로
"""

for test in range(1, 1 + int(input())):
    N = int(input())
    data = list(list(map(int, input().split())) for _ in range(N))
    people = []
    stair = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                people.append((i, j))
            elif data[i][j] :
                stair.append((i, j, data[i][j]))

    temp = []  # 계단마다 각각 걸리는 시간들
    for i in people:
        temp2 = []
        for j in stair:  # 계단은 2개씩
            temp2.append(abs(i[0] - j[0]) + abs(i[1] - j[1]) + j[2] + 1)  # 걸리는 시간
        temp.append(temp2)
    # print(temp)
    #
    result = []
    stair1, stair2 = 0, 0
    tmp = 0  # 몇번째 사람인지
    for i in temp:
        if i[0] < i[1]:  # 몇번 계단을 선택할지
            stair1 += 1
            result.append([i[0], tmp])
        else:
            stair2 += 1
            result.append([i[1], tmp])
        tmp += 1

    result.sort()
    answer = 0
    for i in result:
        if stair1 > 3: # 최대 3명
            stair1 -= 1
            i[0] = min(i[0] + stair[0][2], temp[i[1]][1])  # 계단에 도착해서 대기하는 시간+ 실제 계단 내려가는 시간, 두번째 계단을 선택하는 경우
        if stair2 > 3:
            stair2 -= 1
            i[0] = min(i[0] + stair[1][2], temp[i[1]][0])
    for i in result:
        answer = max(i[0],answer)

    print('#{} {}'.format(test, answer))

