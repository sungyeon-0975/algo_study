import sys
from itertools import combinations
sys.stdin = open('input_4012.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    syn = [[0] * N for _ in range(N)]
    min_ans = 20000

    for i in range(N):
        for j in range(N):
            syn[i][j] = synergy[i][j] + synergy[j][i]

    for com in combinations(range(N), N//2):
        food1, food2 = 0, 0
        num = list(range(N))
        for c in com:
            num.remove(c)
        for i, j in combinations(com, 2):
            food1 += syn[i][j]
        for k, l in combinations(num, 2):
            food2 += syn[k][l]
        if abs(food1 - food2) < min_ans:
            min_ans = abs(food1 - food2)

    print(f'#{t} {min_ans}')