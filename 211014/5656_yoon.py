# import sys
# sys.stdin = open('input.txt')

from collections import deque
from itertools import product
import copy

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    pro = list(product(range(W), repeat=N))                     # 던질 수 있는 모든 경우의 수 뽑기
    cnt_max = 0
    block = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                block += 1

    for p in pro:                                       # ex (0, 0, 0)
        temp = copy.deepcopy(arr)
        cnt = 0
        for idx in p:                                   # ex 0
            q = deque()
            for s in range(H):                          # 행 내려가면서 탐색
                if temp[s][idx] != 0:                   # 0이 아닌 첫번째 벽돌부터
                    cnt += 1
                    q.append((temp[s][idx], s, idx))    # power, i, j
                    temp[s][idx] = 0                    # 벽돌 없애기

                    while q:
                        power, i, j = q.popleft()
                        for pw in range(1, power):      # power만큼 상하좌우 살피며 q에 추가
                            for k in range(4):
                                ni = i + (di[k] * pw)
                                nj = j + (dj[k] * pw)
                                if 0 <= ni < H and 0 <= nj < W and temp[ni][nj] != 0:
                                    q.append((temp[ni][nj], ni, nj))
                                    cnt += 1
                                    temp[ni][nj] = 0
                    break

            for i in range(H-2, -1, -1):
                for j in range(W):
                    if temp[i][j] != 0 and temp[i+1][j] == 0:   # 현재 위치에는 값 있는데 아랫값이 비어있으면
                        for l in range(i+1, H):
                            if l == H-1 and temp[l][j] == 0:    # 맨 아래 칸까지 왔고 0이면 (남은 벽돌 없음)
                                temp[l][j] = temp[i][j]         # 그 위치까지 내려와서 저장
                            elif temp[l][j] != 0:               # 밑으로 내려오다가 0 아닌 값 살아있다면
                                temp[l-1][j] = temp[i][j]       # 그 바로 위에 저장하고 break
                                break
                        temp[i][j] = 0

        if cnt >= cnt_max:
            cnt_max = cnt
        else:
            continue
    print('#{} {}'.format(t, block - cnt_max))
