import sys
sys.stdin = open('12865_input.txt')
# input = sys.stdin.readline

# 226652KB / 6152ms

N, K = map(int, input().split())
bag = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
arr = [[0] * (K+1) for _ in range(N+1)]
# print(bag)

for i in range(1, N+1):
    w, v = bag[i]
    for j in range(1, K+1):
        if j < w:                   # 제한 무게 < 지금 추가할 무게
            arr[i][j] = arr[i-1][j] # 추가 못함
        else:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-w]+v)   # max(추가 안한 가치, 추가 가능한 가치)
    # print(w, v)
    # print(arr[i])
# print(arr)
print(arr[N][K])