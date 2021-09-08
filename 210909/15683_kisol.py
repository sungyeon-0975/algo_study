import sys

# 방법 1: 29200 KB / 324 ms, 방법 2: 29200 KB / 676 ms
# input = sys.stdin.readline
sys.stdin = open('input_15683.txt')

# 방법 1
T = int(input())  # 제출할 때 삭제

for _ in range(T):
    N, M = map(int, input().split())  # N: 행, M: 열
    office = [[6] * (M + 2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M + 2)]
    cctv_d = [
        [],
        [[0], [1], [2], [3]],  # 1번
        [[0, 2], [1, 3]],  # 2번
        [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번
        [[0, 1, 2, 3]]  # 5번(미리처리)
    ]
    cctv_p = []  # cctv 위치 (행, 열)
    cctv_s_check = []  # cctv별로 시작점 체크 리스트
    min_zeros = 0  # 사각지대 최솟값
    dr = [-1, 0, 1, 0]  # 상우하좌(시계방향)
    dc = [0, 1, 0, -1]


    # CCTV 해당 시작점 기준으로 작동시키기
    def Work_CCTV(cctv, start, nr, nc):
        global office
        cnt = 0
        stack = []  # 새로 체크된 공간의 (행, 열)값을 저장
        f_nr, f_nc = nr, nc
        for d in cctv_d[cctv][start]:  # 해당 cctv의 시작점 조합에서 방향 꺼내기
            nr, nc = f_nr, f_nc  # 방향 돌 때 마다 시작점 초기화
            while True:
                nr, nc = nr + dr[d], nc + dc[d]
                if office[nr][nc] == 6:  # 벽이면 break
                    break
                elif office[nr][nc] == 0:  # 공간이면 체크
                    office[nr][nc] = 9  # 감시 체크 (#대신 9를 씀)
                    cnt += 1  # 감시된 공간 수 +1
                    stack.append((nr, nc))  # 감시한 곳 좌표(행, 열) 추가
        return stack, cnt


    # CCTV 5번 해당 시작점 기준으로 작동시키기
    def Work_CCTV_5(cctv, start, nr, nc):
        global office
        f_nr, f_nc = nr, nc
        for d in cctv_d[cctv][start]:  # 해당 cctv의 시작점 조합에서 방향 꺼내기
            nr, nc = f_nr, f_nc  # 방향 돌 때 마다 시작점 초기화
            while True:
                nr, nc = nr + dr[d], nc + dc[d]
                if office[nr][nc] == 6:  # 벽이면 break
                    break
                elif office[nr][nc] == 0:  # 공간이면 체크
                    office[nr][nc] = 9


    # 체크했던 거 되돌리기
    def Work_Back_CCTV(stack):
        global office
        for r, c in stack:
            office[r][c] = 0


    # 최소 사각지대 찾기
    def Find_Min_Zeros(idx):  # idx는 cctv_p의 모든 좌표를 돌 idx
        global min_zeros, cnt_zeros

        if idx == len(cctv_p):  # base case : cctv_p의 모든 좌표를 다 돌았을 때
            if min_zeros > cnt_zeros:
                min_zeros = cnt_zeros
            return

        for i in range(len(cctv_s_check[idx])):  # i는 시작 지점 조합
            if cctv_s_check[idx][i] == 0:  # 해당 시작 지점이 체크 안돼 있으면
                cctv, r, c = cctv_p[idx][0], cctv_p[idx][1], cctv_p[idx][2]  # cctv번호, 행, 열
                cctv_s_check[idx][i] = 1  # 해당 시작 지점 체크
                stack, cnt = Work_CCTV(cctv, i, r, c)  # 해당 시작 지점으로 모든 방향에서 cctv 돌리고 stack 변수에 반환된 stack 저장
                cnt_zeros -= cnt  # 줄어든 사각지대만큼 빼기

                Find_Min_Zeros(idx + 1)  # 그 다음 cctv로 넘어가 확인

                cctv_s_check[idx][i] = 0  # 되돌아오고 해당 지점 체크 해제
                Work_Back_CCTV(stack)  # office도 이전 상태로 되돌리기
                cnt_zeros += cnt  # 다시 되돌려놓은 사각지대만큼 더하기


    # CCTV idx 찾기
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if office[i][j] in range(1, 5):  # cctv 1~4번의 경우 (행, 열)로 위치 저장
                cctv_p.append((office[i][j], i, j))
            elif office[i][j] == 5:  # cctv 5번은 경우의 수가 1번이므로 그냥 바로 cctv 작동
                Work_CCTV_5(5, 0, i, j)

    # 최소 사각지대 값 초기화
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if office[i][j] == 0:
                min_zeros += 1
    cnt_zeros = min_zeros

    # CCTV 종류에 따른 체크 리스트 만들기
    for cctv in cctv_p:
        cctv_s_check.append([0] * len(cctv_d[cctv[0]]))  # cctv의 방향 개수에 따라 체크 리스트 append

    Find_Min_Zeros(0)
    print(min_zeros)

# 방법 2
# T = int(input())  # 제출할 때 삭제
#
# for _ in range(T):
#     N, M = map(int, input().split())  # N: 행, M: 열
#     office = [[6] * (M + 2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M + 2)]
#     cctv_d = [
#         [],
#         [[0], [1], [2], [3]],  # 1번
#         [[0, 2], [1, 3]],  # 2번
#         [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번
#         [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번
#         [[0, 1, 2, 3]]  # 5번(미리처리)
#     ]
#     cctv_p = []  # cctv 위치 (행, 열)
#     cctv_s_check = []  # cctv별로 시작점 체크 리스트
#     min_zeros = N * M  # 사각지대 최솟값
#     dr = [-1, 0, 1, 0]  # 상우하좌(시계방향)
#     dc = [0, 1, 0, -1]
#
#
#     # 사각지대 개수 구하기
#     def Cnt_Zeros(office):
#         cnt_zeros = 0
#         for i in range(1, N + 1):
#             for j in range(1, M + 1):
#                 if office[i][j] == 0:
#                     cnt_zeros += 1
#         return cnt_zeros
#
#
#     # CCTV 해당 시작점 기준으로 작동시키기
#     def Work_CCTV(cctv, start, nr, nc):
#         global office
#         stack = []  # 새로 체크된 공간의 (행, 열)값을 저장
#         f_nr, f_nc = nr, nc
#         for d in cctv_d[cctv][start]:  # 해당 cctv의 시작점 조합에서 방향 꺼내기
#             nr, nc = f_nr, f_nc  # 방향 돌 때 마다 시작점 초기화
#             while True:
#                 nr, nc = nr + dr[d], nc + dc[d]
#                 if office[nr][nc] == 6:  # 벽이면 break
#                     break
#                 elif office[nr][nc] == 0:  # 공간이면 체크
#                     office[nr][nc] = 9
#                     stack.append((nr, nc))
#         return stack
#
#
#     # 체크했던 거 되돌리기
#     def Work_Back_CCTV(stack):
#         global office
#         for r, c in stack:
#             office[r][c] = 0
#
#
#     # 최소 사각지대 찾기
#     def Find_Min_Zeros(idx):  # idx는 cctv_p의 모든 좌표를 돌 idx
#         global min_zeros
#
#         if idx == len(cctv_p):  # base case : cctv_p의 모든 좌표를 다 돌았을 때
#             cnt_zeros = Cnt_Zeros(office)  # 현재 office의 사각지대 구하기
#             if min_zeros > cnt_zeros:
#                 min_zeros = cnt_zeros
#             return
#
#         for i in range(len(cctv_s_check[idx])):  # i는 시작 지점 조합
#             if cctv_s_check[idx][i] == 0:  # 해당 시작 지점이 체크 안돼 있으면
#                 cctv, r, c = cctv_p[idx][0], cctv_p[idx][1], cctv_p[idx][2]  # cctv번호, 행, 열
#                 cctv_s_check[idx][i] = 1  # 해당 시작 지점 체크
#                 stack = Work_CCTV(cctv, i, r, c)  # 해당 시작 지점으로 모든 방향에서 cctv 돌리고 stack 변수에 반환된 stack 저장
#
#                 Find_Min_Zeros(idx + 1)  # 그 다음 cctv로 넘어가 확인
#
#                 cctv_s_check[idx][i] = 0  # 되돌아오고 해당 지점 체크 해제
#                 Work_Back_CCTV(stack)  # office도 이전 상태로 되돌리기
#
#
#     # CCTV idx 찾기
#     for i in range(1, N + 1):
#         for j in range(1, M + 1):
#             if office[i][j] in range(1, 5):  # cctv 1~4번의 경우 (행, 열)로 위치 저장
#                 cctv_p.append((office[i][j], i, j))
#             elif office[i][j] == 5:  # cctv 5번은 경우의 수가 1번이므로 그냥 바로 cctv 작동
#                 Work_CCTV(5, 0, i, j)
#
#     # CCTV 종류에 따른 체크 리스트 만들기
#     for cctv in cctv_p:
#         cctv_s_check.append([0] * len(cctv_d[cctv[0]]))  # cctv의 방향 개수에 따라 체크 리스트 append
#
#     Find_Min_Zeros(0)
#     print(min_zeros)

# 제출용
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())  # N: 행, M: 열
# office = [[6] * (M + 2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M + 2)]
# cctv_d = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]
# cctv_p = []
# cctv_s_check = []
# min_zeros = N * M
# dr = [-1, 0, 1, 0]  # 상우하좌
# dc = [0, 1, 0, -1]
#
# def Cnt_Zeros(office):
#     cnt_zeros = 0
#     for i in range(1, N + 1):
#         for j in range(1, M + 1):
#             if office[i][j] == 0:
#                 cnt_zeros += 1
#     return cnt_zeros
#
# def Work_CCTV(cctv, s, nr, nc):
#     global office
#     stack = []
#     f_nr, f_nc = nr, nc
#     for d in cctv_d[cctv][s]:
#         nr, nc = f_nr, f_nc
#         while True:
#             nr, nc = nr + dr[d], nc + dc[d]
#             if office[nr][nc] == 6:
#                 break
#             elif office[nr][nc] == 0:
#                 office[nr][nc] = 9
#                 stack.append((nr, nc))
#     return stack
#
# def Work_Back_CCTV(stack):
#     global office
#     for r, c in stack:
#         office[r][c] = 0
#
# def Find_Min_Zeros(idx):
#     global min_zeros, office
#     if idx == len(cctv_p):
#         cnt_zeros = Cnt_Zeros(office)
#         if min_zeros > cnt_zeros:
#             min_zeros = cnt_zeros
#         return
#     for i in range(len(cctv_s_check[idx])):  # i는 시작 지점 조합
#         s = cctv_s_check[idx][i]  # 시작 지점
#         if s == 0:
#             cctv, r, c = cctv_p[idx][0], cctv_p[idx][1], cctv_p[idx][2]
#             cctv_s_check[idx][i] = 1
#             stack = Work_CCTV(cctv, i, r, c)
#             Find_Min_Zeros(idx + 1)
#             cctv_s_check[idx][i] = 0
#             Work_Back_CCTV(stack)
#
# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         if office[i][j] == 5:
#             Work_CCTV(5, 0, i, j)
#         elif office[i][j] in range(1, 5):
#             cctv_p.append((office[i][j], i, j))
#
# for cctv in cctv_p:
#     cctv_s_check.append([0] * len(cctv_d[cctv[0]]))
#
# Find_Min_Zeros(0)
# print(min_zeros)
