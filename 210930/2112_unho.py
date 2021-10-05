import sys
from itertools import combinations
sys.stdin = open('input_2112.txt')


def check(e):
    for j in range(W):
        cnt, value, z = 0, 0, 0
        for i in range(D):
            if z < len(e) and i == e[z]:
                if sel[z]:
                    if value == sel[z]:
                        cnt += 1
                    else:
                        cnt = 1
                        value = 1
                else:
                    if value == sel[z]:
                        cnt += 1
                    else:
                        cnt = 1
                        value = 0
                z += 1
            else:
                if value == film[i][j]:
                    cnt += 1
                else:
                    cnt = 1
                    value = film[i][j]

            if cnt == K:                # 최소 갯수 맞으면 반복문 종료
                break
        else:                           # 최소 갯수 안맞으면 함수 종
            return False
    return True


def solution(idx, i):
    global answer, end

    if idx == i:
        for e in li:
            if check(e):
                answer = i
                end = True
        return

    sel[idx] = 1
    solution(idx+1, i)
    if end:
        return

    sel[idx] = 0
    solution(idx+1, i)
    if end:
        return


T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    answer = 0
    end = False

    if not check([]):
        for i in range(1, D+1):
            li = tuple(combinations(range(D), i))
            sel = [0] * i
            solution(0, i)
            
            if end:
                break
    
    print('#{} {}'.format(tc, answer))


"""
1. 약물 투여 결과에 따라 필름 통과 여부 확인하는 함수
2. 약품을 1번 투여부터 시작하여 브루트포스 (곱연산)
"""
# import sys
# from itertools import combinations
# sys.stdin = open('input_2112.txt')


# def check():                                # 합격여부 판단해주는 함수
#     for i in range(W):                      # 열 순환
#         sign = False                        # 해당 열 기준 통과 여부
#         cnt = 0                             # 연속되는 특징 카운트
#         kind = 0                            # 첫번째 특징 설정
#         a = 0

#         for j in range(D):                  # 행 순환
#             if a < n and j == elements[a]:
#                 if sel[a]:
#                     if kind:
#                         cnt += 1
#                     elif not kind:
#                         cnt = 1
#                         kind = 1
                    
#                 else:
#                     if not kind:
#                         cnt += 1
#                     elif kind:
#                         cnt = 1
#                         kind = 0
#                 a += 1

#             else:
#                 if film[j][i] == kind:      # 현재 행이 이전 행과 특징이 같으면
#                     cnt += 1                # 카운트 + 1
#                 else:                       # 이전 행과 다르면
#                     cnt = 1                 # 카운트 초기화 / 이전 특징 초기화
#                     kind = film[j][i]
                
#             if cnt == K:                # 기준 도달시
#                 sign = True             # 해당 열 기준 통과 되어 반복 종료
#                 break
        
#         if not sign:                    # 현재 열이 기준 미달시
#             return False                # 함수 False 반환
    
#     return True                         # 함수 True 반환


# def permu(idx, n):
#     global answer 

#     if idx >= n:
#         if check():
#             answer = n
#             return
#         return

#     for i in range(n):
#         if not sel[i]:
#             sel[i] = 1
#             permu(idx+1, n)

#             if answer != -1:
#                 return
            
#             sel[i] = 0
#             permu(idx+1, n)
            
#             if answer != -1:
#                 return



# T = int(input())

# for tc in range(1, T+1):
#     D, W, K = map(int, input().split())
#     film = [list(map(int, input().split())) for _ in range(D)]
#     end_sign = False
#     answer = -1

#     for a in range(D+1):
#         comb = combinations(range(D), a)
        
#         for elements in comb:
#             n = len(elements)
#             sel = [0] * n
#             permu(0, n)
            
#             if answer != -1:
#                 break

#         if answer != -1:
#             break

    
#     print('#{} {}'.format(tc, answer))