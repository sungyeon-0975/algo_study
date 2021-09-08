import sys

# 29200 KB / 80 ms
# input = sys.stdin.readline
sys.stdin = open('input_1449.txt')

T = int(input())  # 제출할 때 삭제

for _ in range(T):
    N, L = map(int, input().split())
    leaks = sorted(list(map(int, input().split())))
    tapes = 1
    end = leaks[0] + L - 1

    for i in range(1, N):
        if leaks[i] > end:
            tapes += 1
            end = leaks[i] + L - 1

    print(tapes)