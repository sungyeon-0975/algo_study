"""
Memory - 59,512 KB
Time - 187 ms
"""

import sys
sys.stdin = open('input.txt')


def solution(i, j):
    height = land[i[0]][j[0]]                           # 시작 높이는 첫번째 높이로 설정
    cnt = 0

    for k in range(N):
        if land[i[k]][j[k]] == height:                  # 현재 칸이 이전 칸과 높이가 같을때
            cnt += 1
        elif cnt >= 0:                                  # 경
            if abs(land[i[k]][j[k]] - height) > 1:      # 이전 칸과 높이 차이가 1 보다 크면
                return False
            elif land[i[k]][j[k]] < height:             # 현재 칸이 이전 칸보다 나즐때
                cnt = -X+1                              # 높이가 낮아졌으므로 경사로 설치에 앞으로 -x+1 칸이 더 필요함
                height = land[i[k]][j[k]]               
            elif land[i[k]][j[k]] > height:             # 현재 칸이 이전 칸보다 높을때
                if cnt < X:                             # 낮은 곳의 높이가 가로 길이만큼 여유가 없으면 종료
                    return False
                height = land[i[k]][j[k]]
                cnt = 1
        else:                       # 경사로가 튀어 나오거나 안에 못 들어가는 경우
            return False
    if cnt < 0:                     # 경사로가 영역 밖으로 튀어 나오는 경우
        return False

    return True                     # 모든 조건 통과시 경사로 설치 가능


T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        wid = solution([i]*N, range(N))         # 가로
        hei = solution(range(N), [i]*N)         # 세로
        
        answer += wid + hei

    print('#{} {}'.format(tc, answer))