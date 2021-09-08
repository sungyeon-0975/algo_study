import sys
from itertools import permutations

# 530132 KB / 1520 ms ㅠㅠ
# input = sys.stdin.readline
sys.stdin = open('input_14888.txt')

T = int(input())  # 제출할 때 삭제

for _ in range(T):
    N = int(input())  # N: 수의 개수
    A = list(map(int, input().split()))  # 수의 리스트
    operators_num = list(map(int, input().split()))  # 연산자 개수
    operators = []  # Plus(0), Subtract(1), Multiple(2), Divide(3) 연산자
    min_res, max_res = 1000000000, -1000000000
    results = set()  # 결과 계산 담을 세트

    for i in range(4):
        for j in range(operators_num[i]):
            operators.append(i)

    perms = set(list(permutations(operators, N - 1))) # 연산자가 중복돼서 중복된 순열 조합이 나오는 것 방지! 2 1 1 1이면 120가지가 아니라 60가지

    for perm in perms:
        res = A[0]
        for i in range(N - 1):
            if perm[i] == 0:
                res += A[i + 1]
            elif perm[i] == 1:
                res -= A[i + 1]
            elif perm[i] == 2:
                res *= A[i + 1]
            else:
                if res < 0:
                    res = -((-res) // A[i + 1])
                else:
                    res //= A[i + 1]
        results.add(res)

    print(max(results))
    print(min(results))

# [시간초과난 방법]
# for _ in range(T):
#     N = int(input())  # N: 수의 개수
#     A = list(map(int, input().split()))  # 수의 리스트
#     operators_num = list(map(int, input().split()))  # 연산자 개수
#     operators = []  # Plus(0), Subtract(1), Multiple(2), Divide(3) 연산자
#     min_res, max_res = 1000000000, -1000000000
#     res = A[0]  # 임시 저장할 결과값
#     cnt = 0
#
#     for i in range(4):
#         for j in range(operators_num[i]):
#             operators.append(i)
#     operators_check = [0] * len(operators)
#
#
#     def Cal(idx, operator):
#         global res
#         if operator == 0:
#             res += A[idx + 1]
#         elif operator == 1:
#             res -= A[idx + 1]
#         elif operator == 2:
#             res *= A[idx + 1]
#         else:
#             if res < 0:
#                 res = -((-res) // A[idx + 1])
#             else:
#                 res //= A[idx + 1]
#
#
#     def Run_Formular(idx):
#         global res, max_res, min_res, cnt
#
#         if idx == N - 1:
#             cnt += 1
#             if res > max_res:
#                 max_res = res
#             if res < min_res:
#                 min_res = res
#             return
#
#         for i in range(N - 1):
#             if operators_check[i] == 0:
#                 operators_check[i] = 1
#                 temp = res
#                 Cal(idx, operators[i])
#                 Run_Formular(idx + 1)
#                 operators_check[i] = 0
#                 res = temp
#
#
#     Run_Formular(0)
#     print(max_res)
#     print(min_res)
#     print(cnt)


# [dfs 다른 사람 풀이 방법]
# T = int(input())  # 제출할 때 삭제
#
# for _ in range(T):
#     n = int(input())
#     number = list(map(int, sys.stdin.readline().split()))
#     op = list(map(int, sys.stdin.readline().split()))
#     result = set()
#
#
#     def dfs(i, temp, plus, minus, mul, div):
#         if i == n:
#             result.add(temp)
#             return
#
#         if plus:
#             dfs(i + 1, temp + number[i], plus - 1, minus, mul, div)
#         if minus:
#             dfs(i + 1, temp - number[i], plus, minus - 1, mul, div)
#         if mul:
#             dfs(i + 1, temp * number[i], plus, minus, mul - 1, div)
#         if div:
#             if temp < 0:
#                 temp = -(abs(temp) // number[i])
#             else:
#                 temp //= number[i]
#             dfs(i + 1, temp, plus, minus, mul, div - 1)
#
#
#     dfs(1, number[0], op[0], op[1], op[2], op[3])
#     print(max(result))
#     print(min(result))
