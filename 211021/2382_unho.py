from collections import deque
import sys
from pprint import pprint
sys.stdin = open('input.txt')


def move():
    for idx in range(len(stack)):
        r = stack[idx][0] + dr[stack[idx][3]]
        c = stack[idx][1] + dc[stack[idx][3]]

        loc[(stack[idx][0], stack[idx][1])] -= 1
        loc[(r, c)] = loc.get((r, c), 0) + 1
        stack[idx] = [r, c, stack[idx][2], stack[idx][3]]
    stack.sort(key=lambda x: (x[0], x[1], x[2]))


def solution():
    for k, v in loc.items():
        y = k[0]
        x = k[1]

        if v == 1:
            if y == 0 or y == N-1 or x == 0 or x == N-1:
                for idx in range(len(stack)):
                    if stack[idx][0] == y and stack[idx][1] == x:
                        stack[idx][2] //= 2
                        stack[idx][3] = (stack[idx][3]+2) % 4
                        break
        elif v > 1: 
            tmp = [y, x, 0, -1]
            p_li = deque()
            for idx in range(len(stack)):
                if stack[idx][0] == y and stack[idx][1] == x:
                    tmp[2] += stack[idx][2]
                    tmp[3] = stack[idx][3]
                    p_li.appendleft(idx)
            
            for i in p_li:
                stack.pop(i)
            stack.append(tmp)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N, M, K = map(int, input().split())     # 셀의 개수 / 격리 시간 / 미생물 군집의 개수
    loc = {}            # 미생물이 현재 위치 어디 있는지
    stack = []          # 미생물들 리스트
    tc_answer = 0

    for _ in range(K):
        y, x, q, d = map(int, input().split())      # 행 / 열 / 미생물양 / 이동방향
        if d == 1:
            d = 0
        elif d == 3:
            d = 3
        elif d == 4:
            d = 1

        loc[(y, x)] = loc.get((y, x), 0) + 1
        stack.append([y, x, q, d])

    while M > 0:
        move()
        solution()

        M -= 1
    
    for e in stack:
        tc_answer += e[2]
    
    answer.append('#{} {}'.format(tc, tc_answer))
print(*answer, sep='\n')