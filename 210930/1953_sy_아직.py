import sys
sys.stdin = open('input/1953_input.txt')

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
        res = 1
        q = deque([(r + dx[i], c + dy[i], (i + 2) % 4) for i in type[tunnel[r][c]]])
        # print(q)
        for _ in range(l-1):
            print(len(q))
            for _ in range(len(q)):
                x,y, from_d = q.popleft()
                print('type:', tunnel[x][y])
                print(from_d, type[tunnel[x][y]])
                res += 1
                for direction in type[tunnel[x][y]]:
                    if direction != from_d:
                        nx = x + dx[direction]
                        ny = y + dy[direction]
                        opposite = (direction + 2) % 4
                        if -1 < nx < n and -1 < ny < m and (visited[nx][ny] == 0):
                            if (opposite in type[tunnel[nx][ny]]) : #상-하, 좌-우
                                visited[nx][ny] = 1
                                q.append((nx, ny, opposite))
        print('#{} {}'.format(idx, res))