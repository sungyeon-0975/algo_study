import sys

# 달팽이 숫자 채우면서 해당 숫자가 k와 일치 할 경우에 반복문을 종료하고 그 당시의 좌표를 활용해서 구한다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Y, X = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
data = [[0] * Y for _ in range(X)]

if k > X * Y:
    print(0)
    exit()

n = 1
x, y = X - 1, 0
direction = 0

while n != k:
    data[x][y] = n
    nx, ny = x + dx[direction], y + dy[direction]
    if nx < 0 or ny < 0 or nx >= X or ny >= Y or data[nx][ny] != 0:
        direction += 1
        if direction == 4:
            direction = 0
        nx, ny = x + dx[direction], y + dy[direction]
    x, y, n = nx, ny, n + 1

print(f'{y+1} {X-x}')
