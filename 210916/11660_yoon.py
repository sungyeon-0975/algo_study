import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

'''
70044KB / 1296ms
'''

N, M = map(int, input().split())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0] * (N+1))

for i in range(1, N+1):
    for j in range(1, N+1):
        arr[i][j] += arr[i][j-1]

for j in range(1, N+1):
    for i in range(1, N+1):
        arr[i][j] += arr[i-1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
    print(ans)