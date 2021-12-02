# 181236KB	1400ms => pypy3
# 67684KB	5568ms => python3

import sys
input = sys.stdin.readline

def nogada(row, col, n):
    for r in range(row, row + n):
        for c in range(col, col + n):
            if N_list[r][c] != N_list[row][col]:
                nogada(row, col, n//3)
                nogada(row + n//3, col, n//3)
                nogada(row, col + n//3, n//3)
                nogada(row + n//3, col + n//3, n//3)
                nogada(row + (n//3*2), col, n//3)
                nogada(row, col + (n//3*2), n//3)
                nogada(row + (n//3*2), col + (n//3*2), n//3)
                nogada(row + n//3, col + (n//3*2), n//3)
                nogada(row + (n//3*2), col + n//3, n//3)
                return

    result[N_list[row][col]] += 1
    return

N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0, 0]
nogada(0, 0, N)
for i in range(-1,2):
    print(result[i])