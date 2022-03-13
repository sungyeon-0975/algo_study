import sys
sys.stdin = open('1051_input.txt')
# input = sys.stdin.readline

# 30864KB / 68ms

N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]
ans = 1
for i in range(N):
    numbers = input()
    for j in range(M):
        arr[i][j] = int(numbers[j])

stan = N if N < M else M
flag = False
for k in range(stan-1, 0, -1):
    for i in range(N-k):
        for j in range(M-k):
            if arr[i][j] == arr[i+k][j] == arr[i+k][j+k] == arr[i][j+k]:
                ans = (k+1)**2
                flag = True
            if flag: break
        if flag: break
    if flag: break

print(ans)