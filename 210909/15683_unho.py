import sys
from pprint import pprint
sys.stdin = open('input_15683.txt')



def solution(start):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while start:
        node = start.pop()

        for k in range(4):
            y = node[0] + dr[k]
            x = node[1] + dc[k]
                



    


def camera_5(start):                                                # 5번 카메라 감시구역 표시
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while start:
        node = start.pop()

        for k in range(4):
            y = node[0] + dr[k]
            x = node[1] + dc[k]

            while 0 <= y < N and 0 <= x < M and office[y][x] != 6:  # 벽이 나오기 전까지 같은 방향으로 진행
                if not office[y][x]:                                # 0이면 # 으로 변경
                    office[y][x] = 9
                
                y += dr[k]
                x += dc[k]
                



test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(N)]
    coordinate = {}

    for i in range(N):
        for j in range(M):
            if 0 < office[i][j] < 6:
                coordinate[office[i][j]] = coordinate.get(office[i][j], []) + [(i, j)]
    
    camera_5(coordinate.get(5))

    pprint(office)