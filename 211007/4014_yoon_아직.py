import sys
sys.stdin = open('input_4014.txt')

def airstrip(fixed, num): # 고정된 행 또는 열, 몇 번 돌아야 하는지
    cnt = 0
    start = fixed[0]
    for i in range(num):
        if abs(start - fixed[i]) > 1: # 2칸 이상 차이나는 오르막 또는 내리막
            return 0
        else: # 한 칸 내로 차이날 때
            if start - fixed[i] < 0: # 오르막




T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로 test = 행 고정
    # 세로 test = 열 고정
