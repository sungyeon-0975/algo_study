import sys

sys.stdin = open('input_2105.txt')


# POINT) 사각형 모양을 그려야함!!!

# 대각선 오위, 오아, 왼아, 왼위
def dfs(r, c, curr_cnt, direction, d_cnt):
    global max_cnt

    if d_cnt > 4:
        return

    for d in range(2):
        new_d = direction + d
        nr, nc = r + dr[new_d], c + dc[new_d]
        if (nr, nc) == (i, j):
            if curr_cnt > max_cnt:
                max_cnt = curr_cnt
            return
        if 0 <= nr < N and 0 <= nc < N:
            num = arr[nr][nc]  # 디저트 종류
            if not arr_visited[nr][nc] and not type_visited[num] and num > 0:
                arr_visited[nr][nc] = num
                type_visited[num] = 1
                dfs(nr, nc, curr_cnt + 1, new_d, d_cnt + d)
                arr_visited[nr][nc] = 0
                type_visited[num] = 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_visited = [list([0] * N) for _ in range(N)]  # 카페 방문 여부
    type_visited = [0] * 101  # 디저트 종류 선택 여부
    dr = [-1, 1, 1, -1]  # 대각선 오위, 오아, 왼아, 왼위
    dc = [1, 1, -1, -1]
    not_visit_arr = [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]  # 양끝점은 아예 방문하면 안됨
    max_cnt = -1

    # 못갈곳은 0으로 업데이트
    for r, c in not_visit_arr:
        arr[r][c] = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                num = arr[i][j]
                arr_visited[i][j] = num
                type_visited[num] = 1
                dfs(i, j, 1, 0, 1)
                arr_visited[i][j] = 0
                type_visited[num] = 0

    print('#{} {}'.format(t, max_cnt))
