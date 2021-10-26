import sys
sys.stdin = open('1749_input.txt')
# input = sys.stdin.readline
from pprint import pprint

N, M = map(int, input().split())
arr = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
ans = -1E9

for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i][j] - arr[i-1][j-1]
# pprint(arr)
for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(1, i):
            for l in range(1, j):
                if arr[i][j] - arr[k-1][j] - arr[i][l-1] + arr[k-1][j-1] > ans:
                    ans = arr[i][j] - arr[k-1][j] - arr[i][l-1] + arr[k-1][j-1]
print(ans)