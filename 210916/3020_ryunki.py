"""
33104KB , 252ms
"""

import sys

# input = sys.stdin.readline
sys.stdin = open('input_3020.txt')

N, H = map(int, input().split())
obs = [0] * H
min_obs = N // 2  # 0번 구간에서는 최소 반쪽만큼의 수를 가진다.
for i in range(min_obs):  # 밑에서 부터 센다
    obs[int(input())] -= 1  # 밑에서 끝나는 지점은 장애물 1 감소
    obs[H - int(input())] += 1  # 위에서 끝나는 지점은 장애물 1증가

temp = min_obs
cnt = 0
for i in obs:
    temp += i # 증감되는 구간을 더한 뒤
    if temp < min_obs: # 최대최소 비교
        min_obs = temp
        cnt = 1
    elif temp == min_obs:
        cnt += 1

print(min_obs, cnt)

# 메모리 초과
# N, H = map(int, input().split())
# result = [[0] * N for _ in range(H)]
#
# for i in range(N):
#     temp = int(input())
#     if i & 1:
#         for j in range(temp):
#             result[j][i] = 1
#     elif not i & 1:
#         for j in range(temp):
#             result[H - j - 1][i] = 1
#
# temp_list = []
# for i in range(H):
#     result[i] = list(accumulate(result[i]))
#     temp_list.append(result[i][5])
# min_data = min(temp_list)
# print(min_data, temp_list.count(min_data))
