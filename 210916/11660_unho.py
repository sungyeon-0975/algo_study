""" 
memory - 70032 KB
time - 1300 ms
"""

import sys
sys.stdin = open('input.txt')


N, M = map(int, sys.stdin. readline().split())
board = [[0]*(N+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for r in range(1, N+1):
    for c in range(1, N+1):
        board[r][c] = board[r-1][c] + board[r][c-1] - board[r-1][c-1] + board[r][c]

for _ in range(M):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    print(board[y2][x2] + board[y1-1][x1-1] - board[y1-1][x2] - board[y2][x1-1])