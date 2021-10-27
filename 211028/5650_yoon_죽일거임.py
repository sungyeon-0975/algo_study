import sys
sys.stdin = open('5650_input.txt')


dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

hit = {
    1: [(1, 0), (0, -1), (0, 1), (-1, 0)],
    2: [(0, 1), (0, -1), (-1, 0), (1, 0)],
    3: [(0, -1), (1, 0), (-1, 0), (0, 1)],
    4: [(1, 0), (-1, 0), (0, -1), (0, 1)],
    5: [(1, 0), (0, -1), (-1, 0), (0, 1)],
}

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    score = 0

    wormhole = [[] for _ in range(5)]

    for i in range(N):
        for j in range(N):
            if 5 < arr[i][j] < 11:
                wormhole[arr[i][j]-6].append((i, j))

    for r in range(N):
        for c in range(N):
            if not arr[r][c]:
                for k in range(4):
                    di, dj = dir[k]
                    temp_score = 0
                    nr, nc = r, c
                    if nr + di < 0 or nr + di >= N or nc + dj < 0 or nc + dj >= N:
                        continue
                    while True:
                        nr = nr + di
                        nc = nc + dj
                        if 0 <= nr < N and 0 <= nc < N:
                            if nr == r and nc == c:
                                break
                            elif arr[nr][nc] == -1:
                                break
                            elif 0 < arr[nr][nc] < 6:
                                temp_score += 1
                                di, dj = hit[arr[nr][nc]][dir.index((di, dj))]
                            elif 5 < arr[nr][nc] < 11:
                                nr, nc = wormhole[arr[nr][nc]-6][(wormhole[arr[nr][nc]-6].index((nr, nc)) + 1) % 2]
                        else:
                            temp_score += 1
                            nr = nr - di
                            nc = nc - dj
                            di, dj = dir[(dir.index((di, dj)) + 2) % 4]
                    if temp_score > score:
                        score = temp_score

    print('#{} {}'.format(t, score))