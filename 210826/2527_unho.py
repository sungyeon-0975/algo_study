'''
#1. 2차원 배열 이용하여 사각형의 영역에 +1 을 하여, 겹치는 부분이 숫자 2가 되는경우
-> 비교적 간단하게 구현 가능하나, 조건이 까다로워 여러 유형을 걸러내기 어려워 많은 반례를 생각해야함
-> 좌표값이 50,000 * 50,000 으로 최악의 경우, 50,000(가로) * 50,000(세로) * 2(사각형 두개) = 약 5,000,000,000번 (50억번) 연산을 하게 됨 -> 약 5초 -> 시간 제한에 걸림

#2. 숫자 연산을 통해 계산
생각해야 할 반례
1. 첫번쨰 사각형과 두번째 사각형 중 어느게 큰 값이 오게 될지
2. 조건이 꽤 여러가지가 나오게 됨
'''

import sys


# 숫자 연산 통한 풀형
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, sys.stdin.readline().split())
    
    if (x1 > p2) or (p1 < x2) or (y1 > q2) or (q1 < y2):                                                            # 공통 부분이 없음
        answer = 'd'
    elif (x1 == p2 and y1 == q2) or (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2):  # 점
        answer = 'c'
    elif (x1 == p2) or (y1 == q2) or (p1 == x2) or (q1 == y2):                                                      # 선
        answer = 'b'
    else:                                                                                                           # 직사각형
        answer = 'a'
    
    print(answer)
        






# 2차원 배열 이용한 단순 계산
'''
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, sys.stdin.readline().split())

    board = [[0] * (max(x1, x2, p1, p2)+1) for _ in range(max(y1, y2, q1, q2) + 1)]
    two_cnt = line_cnt = pre_two_cnt = 0
    sign = False
    answer = ''

    # 첫번째 사각형
    for i in range(y1, q1+1):
        for j in range(x1, p1+1):
            board[i][j] += 1
    
    # 두번째 사각형
    for i in range(y2, q2+1):
        for j in range(x2, p2+1):
            board[i][j] += 1

    # 겹치는 부분 탐색
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                two_cnt += 1
        if two_cnt == 1:
            sign = True

        if pre_two_cnt != two_cnt:
            line_cnt += 1
            pre_two_cnt = two_cnt
    

    if line_cnt > 1 and sign == False:
        answer = 'a'
    elif two_cnt == 0:
        answer = 'd'
    elif two_cnt == 1:
        answer = 'c'
    elif two_cnt > 1:
        answer = 'b'
    
    print(answer)
'''