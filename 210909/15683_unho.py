""" 
브루트포스
DFS
Deepcopy

5번 카메라는 4방향을 모두 보기 때문에 5번 카메라의 영역은 모두 변경해주고 시작한다.
1,2,3,4 카메라는 90도를 회전하면서 확인 해야함

재귀
- idx 가 모든 카메라 갯수를 넘으면 보드에서 0의 갯수 카운트 / DFS 하나 종료
- 순열 구하는 재귀 (x) 너무 느림
- 처음에 5번 카메라 지우고 4번, 3번 순서대로 지우는걸 생각했으나, 예외 상황이 발견됨



Memory - 29200 KB
Time - 1252 ms

최적화... 어떻게 할지 감이 안잡힘ㅠ

"""


import sys
from pprint import pprint
sys.stdin = open('input_15683.txt')



def solution(idx):
    global answer

    if idx == n_len:
        tmp = 0 
        for y in range(N):
            for x in range(M):
                if office[y][x] == 0:
                    tmp += 1
        if answer > tmp:
            answer = tmp
        # pprint(office)
        return

    else:
        camera(coordinate[idx], idx)
        solution(idx+1)
        restore(idx+7)
        kind_plus(coordinate[idx][0])

        camera(coordinate[idx], idx)
        solution(idx+1)
        restore(idx+7)
        kind_plus(coordinate[idx][0])

        camera(coordinate[idx], idx)
        solution(idx+1)
        restore(idx+7)
        kind_plus(coordinate[idx][0])

        camera(coordinate[idx], idx)
        solution(idx+1)
        restore(idx+7)
        kind_plus(coordinate[idx][0])



def camera(coordinate_arr, idx):
    for k in kind[coordinate_arr[0]]:
        y = coordinate_arr[1] + dr[k]
        x = coordinate_arr[2] + dc[k]

        while 0 <= y < N and 0 <= x < M and office[y][x] != 6:
            if not office[y][x]:
                office[y][x] = idx+7

            y += dr[k]
            x += dc[k]



def restore(idx):
    for i in range(N):
        for j in range(M):
            if office[i][j] == idx:
                office[i][j] = 0



def kind_plus(camera_num):
    for i in range(len(kind[camera_num])):
        kind[camera_num][i] = (kind[camera_num][i]+1) % 4



def camera_5(start):                                                # 5번 카메라 감시구역 표시
    while start:
        node = start.pop()
        for k in range(4):
            y = node[0] + dr[k]
            x = node[1] + dc[k]

            while 0 <= y < N and 0 <= x < M and office[y][x] != 6:  # 벽이 나오기 전까지 같은 방향으로 진행
                if not office[y][x]:                                # 0이면 # 으로 변경
                    office[y][x] = 5
                
                y += dr[k]
                x += dc[k]



dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]



test_case = int(input())

for _ in range(test_case):

    N, M = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(N)]
    coordinate = []
    five = []
    kind = [0, [0], [0, 2], [0, 1], [0, 1, 2]]
    answer = N * M


    for i in range(N):
        for j in range(M):
            if 0 < office[i][j] < 5:
                coordinate.append((office[i][j], i, j))
            elif office[i][j] == 5:
                five.append((i, j))
                
    camera_5(five)
    n_len = len(coordinate)                

    solution(0)

    print(answer)