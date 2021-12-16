import sys
input = sys.stdin.readline

# 29452KB	76ms

# 구글링
N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    N_list[i][1] = min(N_list[i - 1][0], N_list[i - 1][2]) + N_list[i][1]
    N_list[i][0] = min(N_list[i - 1][1], N_list[i - 1][2]) + N_list[i][0]
    N_list[i][2] = min(N_list[i - 1][0], N_list[i - 1][1]) + N_list[i][2]
print(min(N_list[N - 1][0], N_list[N - 1][1], N_list[N - 1][2]))



# 시간 초과
# def bfs(cnt, n, col):
#     global result
#     if result < n:
#         return
#
#     if cnt == N:
#         result = n
#         return
#
#     for k in range(3):
#         if k != col:
#             bfs(cnt + 1, n + N_list[cnt][k], k)
#
# N = int(input())
# N_list = [list(map(int, input().split())) for _ in range(N)]
# result = 1e9
# for i in range(3):
#     bfs(1, N_list[0][i], i)
# print(result)