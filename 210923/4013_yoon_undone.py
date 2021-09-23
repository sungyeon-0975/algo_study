import sys
sys.stdin = open('input_4013.txt')

# 일단 포기

def spin(num, dir, k):
    global idx

T = int(input())
for t in range(1, T+1):
    K = int(input())
    # N극 0, S극 1, 2-6 맞닿아있음
    mag = [[]] + [list(map(int, input().split())) for _ in range(4)] # 2번
    idx = [0] * (K+1)
    for _ in range(K):
        num, dir = map(int, input().split())
        if 1 < num and mag[num-1][(idx[num-1]+2) % 8] != mag[num][(idx[num]+6) % 8]:
            spin(num-1, -1*dir, -1)
        if num < 4 and mag[num-1][(idx[num-1]+6) % 8] != mag[num][(idx[num]+2) % 8]:
            spin(num+1, -1*dir, 1)