"""
Memory - 117,376 kb
Time - 8,088 ms

다시 풀고 싶지 않은 문제..
"""


import sys
from collections import deque
sys.setrecursionlimit(20000)
sys.stdin = open('input.txt')


def boom(e, height, move):
    global tmp_board

    for i in range(move):
        if height-i >= 0:
            tmp_move = tmp_board[e][height-i]
            tmp_board[e][height-i] = 0
            if tmp_move > 1:
                boom(e, height-i, tmp_move)

        if height+i < len(tmp_board[e]):
            tmp_move = tmp_board[e][height+i]
            tmp_board[e][height+i] = 0
            if tmp_move > 1:
                boom(e, height+i, tmp_move)
        
        if e-i >= 0 and len(tmp_board[e-i]) > height:
            tmp_move = tmp_board[e-i][height]
            tmp_board[e-i][height] = 0
            if tmp_move > 1:
                boom(e-i, height, tmp_move)
        
        if e+i < W and len(tmp_board[e+i]) > height:
            tmp_move = tmp_board[e+i][height]
            tmp_board[e+i][height] = 0
            if tmp_move > 1:
                boom(e+i, height, tmp_move)


def solution(arr):
    global tmp_board

    tmp_board = {}
    for a in range(W):
        tmp_board[a] = board[a].copy()

    # print('----- inital -----')
    # for i in range(H):
    #     print(i, tmp_board[i])
    # print()        

    for e in arr:                           # 초기 구슬 떨어짐
        height = len(tmp_board[e]) - 1      # 초기 터지는 블럭의 높이 인덱스
        if height < 0:
            break
        move = tmp_board[e][height]         # 초기 터지는 블럭의 범위
        tmp_board[e][height] = 0

        for i in range(move):
            if 0 <= e-i and len(tmp_board[e-i]) > height:
                tmp_move = tmp_board[e-i][height]
                tmp_board[e-i][height] = 0
                if tmp_move > 1:
                    boom(e-i, height, tmp_move)

            if e+i < W and len(tmp_board[e+i]) > height:
                tmp_move = tmp_board[e+i][height]
                tmp_board[e+i][height] = 0
                if tmp_move > 1:
                    boom(e+i, height, tmp_move)

            if height-i >= 0:
                tmp_move = tmp_board[e][height-i]
                tmp_board[e][height-i] = 0
                if tmp_move > 1:
                    boom(e, height-i, tmp_move)
        
        for i in range(W):
            while tmp_board[i].count(0) > 0:
                tmp_board[i].remove(0)

        # print('----- 진행 -----')
        # for i in range(H):
        #     print(i, tmp_board[i])
        # print()


def case(idx, arr):             # 구슬이 떨어지는 경우들을 구해줌
    global tmp_board, tc_answer

    if idx >= N:
        tmp_board = {}
        for a in range(W):
            tmp_board[a] = board[a].copy()
        solution(arr)
        
        cnt = 0
        for i in range(W):
            cnt += len(tmp_board[i])
        
        if tc_answer > cnt:
            tc_answer = cnt

        return
    
    for i in range(W):
        arr.append(i)
        case(idx+1, arr)
        arr.pop()


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())     # 구슬 떨어뜨리는 횟수 / 가로 / 세로
    board = {i:deque() for i in range(W)}
    tmp_board = {}
    tc_answer = 1e10

    for _ in range(H):
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)):
            if tmp[j]:
                board[j].appendleft(tmp[j])
    
    case(0, [])

    print('#{} {}'.format(tc, tc_answer))