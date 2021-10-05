"""
Memory - 63,940 KB
Time - 316 ms
"""

import sys
from pprint import pprint
sys.stdin = open('input.txt')


def powerset(idx):                          # 부분집합 구하기
    global tmp_max_sum

    if idx >= M:
        sel = []
        tmp = 0
        for a in range(M):
            if visit[a]:
                sel.append(hive[i][j:j+M][a])
        
        if sum(sel) <= C:                   # 해당 부분집합이 기준 통과시
            for a in range(len(sel)):       # 해당 부분집합의 통 크기별 가중치 가격 구함
                tmp += sel[a] ** 2
            if tmp > tmp_max_sum:           # 다른 부분집합보다 값이 크면 새로 저장
                tmp_max_sum = tmp
        return
    
    visit[idx] = 1
    powerset(idx+1)
    visit[idx] = 0
    powerset(idx+1)


def search():                       # 최고 가격 좌표값들 골라서 순회
    global answer

    while max_li:
        node = max_li.pop()

        tmp = 0
        for i in range(N):
            for j in range(N):
                if i == node[0] and (j-M+1 <= node[1] < j+M):       # 최고 가격을 선택해서 못선택하는 범위일때
                    continue
                if price[i][j] > tmp:
                    tmp = price[i][j]
        
        if answer < (max_price + tmp):
            answer = max_price + tmp

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())                             # 벌통 크기 / 채취 길이 / 채취 최대 양
    hive = [list(map(int, input().split())) for _ in range(N)]      # 벌통
    price = [[0] * N for _ in range(N)]
    max_price, max_li = 0, []
    answer = 0

    for i in range(N):              # 벌통 순회
        for j in range(N-M+1):
            if sum(hive[i][j:j+M]) <= C:                    # 채취 기준 미달시
                for k in range(M):                          # 채취 길이만큼 순회하여 통별 크기^2 의 가격을 합침
                    price[i][j] += (hive[i][j+k] ** 2)

            else:                                           # 채취 기준 초과시
                visit = [0] * M
                tmp_max_sum = 0
                powerset(0)                                 # 경우의 수 모두 탐색
                price[i][j] = tmp_max_sum

            if price[i][j] >= max_price:                    # 현재가 가장 높은 가격이면
                if price[i][j] > max_price:
                    max_li.clear()
                max_price = price[i][j]                     # 가격 갱신 및 좌표값 추가
                max_li.append((i, j))
    
    search()
    
    print('#{} {}'.format(tc, answer))