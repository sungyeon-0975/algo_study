import sys

# 30864KB / 164ms Python3
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_10819.txt')


def permutations(idx, temp):
    global res

    if idx == len(arr):
        if temp > res:
            res = temp

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            new_arr[idx] = arr[i]
            permutations(idx + 1, temp + abs(new_arr[idx] - new_arr[idx - 1]))  # 이전 값과 현재 값의 절대값을 더해가면서 재귀 호출
            visited[i] = 0


N = int(input())
arr = list(map(int, input().split()))
res = 0
visited = [0] * N
new_arr = [0] * N  # 새로운 순열로 만들 리스트

# 첫 번째 숫자 정하기
for i in range(N):
    visited[i] = 1
    new_arr[0] = arr[i]
    permutations(1, 0)
    visited[i] = 0

print(res)


# 1차 204ms
# def permutations(idx):
#     global res
#
#     if idx == len(arr):
#         temp = 0
#         for j in range(len(arr) - 1):
#             temp += abs(new_arr[j] - new_arr[j + 1])
#         if temp > res:
#             res = temp
#
#     for i in range(len(arr)):
#         if not visited[i]:
#             visited[i] = 1
#             new_arr[idx] = arr[i]
#             permutations(idx + 1)
#             new_arr[idx] = 0
#             visited[i] = 0
#
#
# N = int(input())
# arr = list(map(int, input().split()))
# res = 0
# visited = [0] * N
# new_arr = [0] * N
#
# permutations(0)
#
# print(res)


# 완전탐색으로 안해도 될까 싶어 시도해봤던 방법
# for i in range(len(arr) - 1):
#     idx = i
#     if i % 2:
#         for j in range(i + 1, len(arr)):
#             if arr[idx] < arr[j]:
#                 idx = j
#     else:
#         for j in range(i + 1, len(arr)):
#             if arr[idx] > arr[j]:
#                 idx = j
#     arr[idx], arr[i] = arr[i], arr[idx]

