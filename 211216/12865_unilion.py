import sys
input = sys.stdin.readline

# KB ms

N, K = map(int, input().split()) # 물품의 수 , 버틸 수 있는 무게
N_list = [[0, 0]]
for _ in range(N):
    N_list.append(list(map(int, input().split())))
temp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        W = N_list[i][0]
        V = N_list[i][1]

        if j < W:
            temp[i][j] = temp[i - 1][j]
        else:
            temp[i][j] = max(V + temp[i - 1][j - W], temp[i - 1][j])
print(temp[N][K])