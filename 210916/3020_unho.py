'''
memory - 96756 KB
time - 1320 ms
'''


import sys
sys.stdin = open('input.txt')


N, H = map(int, sys.stdin.readline().split())
cave = [[0] * 3 for _ in range(H+1)]
min_ans = N
answer = 1


for idx in range(1, N+1):
    num = int(sys.stdin.readline())

    if idx%2:           # odd / bottom start
        cave[H-num+1][1] += 1
        cave[H-num+1][2] -= 1

    elif not idx%2:     # even / top start        
        cave[1][1] += 1
        cave[1][2] -= 1
        if num < H:
            cave[num+1][1] -= 1
            cave[num+1][2] += 1

for r in range(1, H+1):
    for c in range(1, 3):
        cave[r][c] = cave[r-1][c] + cave[r][c-1] - cave[r-1][c-1] + cave[r][c]
    
    tmp = cave[r][1]

    if tmp < min_ans:
        min_ans = tmp
        answer = 1
    elif tmp == min_ans:
        answer += 1

print(min_ans, answer)



# 2차원 누적합으로 구함
""" import sys
sys.stdin = open('input.txt')


N, H = map(int, sys.stdin.readline().split())
cave = [[0] * (N+2) for _ in range(H+1)]
min_ans = N
answer = 1

for c in range(1, N+1):
    num = int(sys.stdin.readline()) # size
    
    if not c%2:                     # even / top start
        cave[1][c] += 1
        cave[1][c+1] -= 1
        if num < H:
            cave[num+1][c] -= 1
            cave[num+1][c+1] += 1

    elif c%2:                       # odd / bottom start
        cave[H-num+1][c] += 1
        cave[H-num+1][c+1] -= 1


for r in range(1, H+1):             # accumulate sum
    tmp = 0
    for c in range(1, N+2):
        cave[r][c] = cave[r-1][c] + cave[r][c-1] - cave[r-1][c-1] + cave[r][c]
        if cave[r][c]:
            tmp += 1

    if tmp < min_ans:
        min_ans = tmp
        answer = 1
    elif tmp == min_ans:
        answer += 1

print(min_ans, answer) """