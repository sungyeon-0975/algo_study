"""
1. 약물 투여 결과에 따라 필름 통과 여부 확인하는 함수
2. 약품을 1번 투여부터 시작하여 브루트포스 (곱연산)
"""

import sys
from itertools import combinations
sys.stdin = open('input_2112.txt')


def check():                         # 합격여부 판단해주는 함수
    for i in range(W):                  # 열 순환
        sign = False                    # 해당 열 기준 통과 여부
        cnt = 0                         # 연속되는 특징 카운트
        kind = film[0][i]                # 첫번째 특징 설정

        for j in range(D):           # 행 순환
            if j in elements:
                if sel[elements.index(j)]:
                    if kind == 1:
                        cnt += 1
                    else:
                        cnt = 1
                        kind = 1
                else:
                    if kind == 0:
                        cnt += 1
                    else:
                        cnt = 1
                        kind = 0
                
                if cnt == K:
                    sign = True
                    break

            else:
                if film[j][i] == kind:       # 현재 행이 이전 행과 특징이 같으면
                    cnt += 1                # 카운트 + 1
                else:                       # 이전 행과 다르면
                    cnt = 1                 # 카운트 초기화 / 이전 특징 초기화
                    kind = film[j][i]
                
                if cnt == K:                # 기준 도달시
                    sign = True             # 해당 열 기준 통과 되어 반복 종료
                    break
        
        if not sign:                    # 현재 열이 기준 미달시
            return False                # 함수 False 반환
    
    else:                               # 모든 열이 기준 통과시
        return True                     # 함수 True 반환


def solution(idx, a):
    global end_sign, answer
    if idx >= a:
        if check():
            end_sign = True
            answer = a
        return

    for s in range(len(sel)):
        if not sel[s]:
            sel[s] = True
            solution(idx+1, a)

            if end_sign:
                return
            
            sel[s] = False
            solution(idx+1, a)
        
            if end_sign:
                return


T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    end_sign = False
    answer = -1

    for a in range(D+1):
        comb = combinations(range(D), a)
        
        for elements in comb:
            sel = [False] * len(elements)
            solution(0, a)

            if end_sign:
                break

        if end_sign:
            break
    
    print('#{} {}'.format(tc, answer))