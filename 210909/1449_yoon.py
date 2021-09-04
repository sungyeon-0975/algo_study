import sys
# input = sys.stdin.readline
sys.stdin = open('input_1449.txt')

'''
29200KB / 88ms
'''

T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    leak = list(map(int, input().split()))
    leak.sort()
    start = leak[0] - 0.5
    end = start + L
    cnt = 1

    for n in range(N):
        if start <= leak[n] <= end:
            continue
        else:
            start = leak[n] - 0.5
            end = start + L
            cnt += 1

    print(cnt)