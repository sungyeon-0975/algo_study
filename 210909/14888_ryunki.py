import sys

sys.stdin = open('input_14888.txt')

"""
pypy3 : 681036KB 2856ms
python3: 29200KB 92ms

"""


def DFS(start, index, plus, minus, multi, div):
    global my_max, my_min
    if index >= N:
        if my_max < start:
            my_max = start
        if my_min > start:
            my_min = start

    else:
        if plus:
            DFS(start + numbers[index], index + 1, plus - 1, minus, multi, div)
        if minus:
            DFS(start - numbers[index], index + 1, plus, minus - 1, multi, div)
        if multi:
            DFS(start * numbers[index], index + 1, plus, minus, multi - 1, div)
        if div:
            DFS(int(start / numbers[index]), index + 1, plus, minus, multi, div - 1)


for test in range(1, 1 + int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))
    plus, minus, multi, div = map(int, input().split())
    my_max = float('-inf')
    my_min = float('inf')

    DFS(numbers[0], 1, plus, minus, multi, div)

    print(my_max)
    print(my_min)
#
# from itertools import permutations
#
# for test in range(1, 1 + int(input())):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     operations = list(map(int, input().split()))
#
#     # 0:+      1:-     2:*    3://
#     oper_temp = []
#     for x, y in enumerate(operations):
#         while y:
#             oper_temp.append(x)
#             y -= 1
#     oper_c = list(permutations(oper_temp, len(oper_temp)))
#
#     my_max = float('-inf')
#     my_min = float('inf')
#
#     for i in range(len(oper_c)):
#         result = numbers[0]
#
#         for j in range(1, N):
#             if oper_c[i][j - 1] == 0:
#                 result = result + numbers[j]
#             elif oper_c[i][j - 1] == 1:
#                 result = result - numbers[j]
#             elif oper_c[i][j - 1] == 2:
#                 result = result * numbers[j]
#             elif oper_c[i][j - 1] == 3:
#                 result = int(result/numbers[j])
#
#         if my_max < result:
#             my_max = result
#         if my_min > result:
#             my_min = result
#
#     print(my_max)
#     print(my_min)
