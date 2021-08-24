import sys

# 달팽이 숫자 채우면서 해당 숫자가 k와 일치 할 경우에 반복문을 종료하고 그 당시의 좌표를 활용해서 구한다.

dx = [-1, 0, 1, 0] # 방향 위 오른 아래 왼
dy = [0, 1, 0, -1]
Y, X = map(int, sys.stdin.readline().split()) # X 가 결국 세로 인덱스 Y가 가로 인덱스
k = int(sys.stdin.readline())
data = [[0] * Y for _ in range(X)] # 초기화

if k > X * Y: # 찾고자 하는 수가 범위를 벗어나는 경우는 0
    print(0)
    exit()

n = 1
x, y = X - 1, 0  # 6,0    ->  1 ,1    -> y+1 , X-x
direction = 0

while n != k:
    data[x][y] = n # 1,1에 즉 사각형 왼쪽 아래부터 시작
    nx, ny = x + dx[direction], y + dy[direction]

    # 범위를 벗어나거나 값이 0이 아니면 방향을 전환한다.
    if nx < 0 or ny < 0 or nx >= X or ny >= Y or data[nx][ny] != 0:
        direction += 1
        if direction == 4:
            direction = 0
        nx, ny = x + dx[direction], y + dy[direction]
    x, y = nx, ny
    n += 1
# print(x,y)
print(f'{y + 1} {X - x}') # 위치조정 전치행렬 + y가 0부터 시작했으므로 1인덱스 증가 + 6-0,6-1,
