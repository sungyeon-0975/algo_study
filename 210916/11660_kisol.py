import sys

# PyPy3: 136676 KB / 516 ms, Python3: 70048 KB / 1152 ms Thanks to 지윤
# input = sys.stdin.readline
sys.stdin = open('input_11660.txt')

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    grid = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            grid[i][j] += grid[i][j - 1]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            grid[i][j] += grid[i - 1][j]

    for i in range(M):
        r1, c1, r2, c2 = map(int, input().split())
        result = grid[r2][c2] - grid[r1 - 1][c2] - (grid[r2][c1 - 1] - grid[r1 - 1][c1 - 1])
        print(result)
