import sys

# 29484KB / 68ms Python3
# input = sys.stdin.readline
'''
d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것
현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색

1) 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
2) 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
3) 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
4) 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
'''

sys.stdin = open('input_14503.txt')


def dfs():
    global cnt, r, c, d

    # 청소가 안 돼있는 경우, 청소 처리
    if not arr[r][c]:
        cnt += 1
        arr[r][c] = 2

    # i : 시작방향(현재 방향 기준 왼쪽방향), j : 종료 방향
    i, j = d + 3, d - 1
    while i != j:
        direction = i % 4
        nr, nc = r + dr[direction], c + dc[direction]
        # 해당 위치 청소가 안 돼있는 경우, 이동
        if not arr[nr][nc]:
            d, r, c = direction, nr, nc
            dfs()
            # 현재 방향 기준으로 뒤로 왔을 때 벽인 경우, return
            if arr[r - dr[d]][c - dc[d]] == 1:
                return
            # 벽이 아닌 경우, 이동 후 방향 다시 설정. (i의 경우 뒤에 -1을 해주고 시작하기 때문에 +3이 아니라 +4 처리)
            r, c = r - dr[d], c - dc[d]
            i, j = d + 4, d - 1
        i -= 1  # 청소가 돼있거나 벽인 경우 왼쪽으로 방향 이동

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # 0: 청소안됨, 1: 벽, 2: 청소됨
cnt = 0
dr = [-1, 0, 1, 0] # 북동남서
dc = [0, 1, 0, -1]

dfs()
print(cnt)
