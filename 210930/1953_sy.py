import sys
sys.stdin = open('input_1953.txt')

from collections import deque

if __name__ == "__main__":
    dx = [-1, 0, 1, 0]#상, 우, 하, 좌
    dy = [0, 1, 0, -1]
    type = [[],
            [0, 1, 2, 3],
            [0, 2],
            [3, 1],
            [0, 1],
            [2, 1],
            [2, 3],
            [0, 3]]
    t = int(input())
    for idx in range(1, t+1):
        n, m, r, c, l = map(int, input().split())
        tunnel = [list(map(int, input().split())) for _ in range(n)]
        visited = [[0]* m for _ in range(n)]
        res = 0
        visited[r][c] = 1
        q = deque([(r, c)])
        for _ in range(l):
            for _ in range(len(q)):
                x,y = q.popleft()
                res += 1
                for direction in type[tunnel[x][y]]:
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    opposite = (direction + 2) % 4
                    if -1 < nx < n and -1 < ny < m and (visited[nx][ny] == 0) and (opposite in type[tunnel[nx][ny]]) : #상-하, 좌-우
                        visited[nx][ny] = 1
                        q.append((nx, ny))
        print('#{} {}'.format(idx, res))