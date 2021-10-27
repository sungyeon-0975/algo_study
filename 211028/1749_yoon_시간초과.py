import sys
sys.stdin = open('1749_input.txt')
# input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
ans = -1E9

for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] = arr[i][j] + arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]

for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(i, N+1):
            for l in range(j, M+1):
                temp = arr[k][l] - arr[k][j-1] - arr[i-1][l] + arr[i-1][j-1]
                if temp > ans:
                    ans = temp

print(ans)