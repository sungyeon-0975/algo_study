"""
Memory - 70000 KB
Time - 1272 ms
"""

import sys


N, M = map(int, sys.stdin.readline().split())
board = [[0] * (M+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, M+1):
        board[i][j] = board[i][j] + board[i][j-1] + board[i-1][j] - board[i-1][j-1]


K = int(sys.stdin.readline())
for _ in range(K):
    y, x, q, p = map(int, sys.stdin.readline().split())

    if y <= 0 or x <=0:
        print(0)
    
    print(board[q][p] - board[y-1][p] - board[q][x-1] + board[y-1][x-1])