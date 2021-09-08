'''
itertools 활용
Memory - 35088 KB
Time - 656 ms

순열 재귀로 직접 구현
Memory - 35088 KB
Time - 7580 ms
'''


""" recursion """
import sys
sys.stdin = open('input_14888.txt')


def solution(idx, ans, pre):
    # Base Case
    if idx == N-1:
        answer.append(ans)
        return

    for k in range(N-1):
        if not select[k]:
            ans = pre
            select[k] = 1
            tmp = op[k]
            
            if tmp == '*':
                ans *= n_list[idx+1]
            elif tmp == '/':
                ans = int(ans/n_list[idx+1])
            elif tmp == '+':
                ans += n_list[idx+1]
            elif tmp == '-':
                ans -= n_list[idx+1]

            solution(idx+1, ans, ans)            
            select[k] = 0



test_case = int(input())

for _ in range(test_case):
    N = int(input())
    n_list = list(map(int, input().split()))
    in_op = list(map(int, input().split()))
    op = []
    select = [0] * N
    tmp = ''
    answer = []

    for i in range(4):
        if i == 0:
            c = '+'
        elif i == 1:
            c = '-'
        elif i == 2:
            c = '*'
        elif i == 3:
            c = '/'

        op.extend(c * in_op[i])
    
    solution(0, n_list[0], n_list[0])

    print(max(answer))
    print(min(answer))


""" permutation recursion """
# import sys
# sys.stdin = open('input_14888.txt')


# def permu(idx):                     # 재귀로 순열 구함
#     # Base Case
#     if idx == N-1:
#         operators.add(tuple(tmp))
#         return

#     for k in range(N-1):
#         if not select[k]:
#             tmp.append(op[k])
#             select[k] = 1
#             permu(idx+1)
#             tmp.pop()
#             select[k] = 0


# test_case = int(input())

# for _ in range(test_case):
#     N = int(input())
#     n_list = list(map(int, input().split()))
#     in_op = list(map(int, input().split()))
#     op = []
#     operators = set()
#     select = [0] * N
#     tmp = []


#     for i in range(4):
#         if i == 0:
#             c = '+'
#         elif i == 1:
#             c = '-'
#         elif i == 2:
#             c = '*'
#         elif i == 3:
#             c = '/'

#         op.extend(c * in_op[i])

#     permu(0)        # 연산자들 순열로 경우의 수 구함

#     answer = []
#     for e in operators:
#         tmp_answer = n_list[0]
#         for j in range(len(e)):
#             if e[j] == '+':
#                 tmp_answer += n_list[j+1]
#             elif e[j] == '-':
#                 tmp_answer -= n_list[j+1]
#             elif e[j] == '*':
#                 tmp_answer *= n_list[j+1]
#             elif e[j] == '/':    
#                 tmp_answer = int(tmp_answer/n_list[j+1])    # 음수에도 0에 가깝게 나눗셈 위해
        
#         answer.append(tmp_answer)
        
#     print(max(answer))
#     print(min(answer))



""" itertools """
# import sys
# import itertools
# sys.stdin = open('input_14888.txt')

# test_case = int(input())

# for _ in range(test_case):
#     N = int(input())
#     n_list = list(map(int, input().split()))    # 숫자 리스트
#     operator = list(map(int, input().split()))  # 연산자 리스트 (덧셈 / 뺄셈 / 곱셈 / 나눗셈)
#     op = []

#     for idx in range(4):                        # 연산자들을 리스트 리스트로
#         if idx == 0:
#             c = '+'
#         elif idx == 1:
#             c = '-'
#         elif idx == 2:
#             c = '*'
#         elif idx == 3:
#             c = '/'
        
#         op.extend(c*operator[idx])

#     permu = set(itertools.permutations(op, len(op)))    # 순열 구함, 중복 제거

#     answer = []
#     for e in permu:                                     # 앞에서부터 계산
#         tmp_answer = n_list[0]
#         for j in range(len(e)):
#             if e[j] == '+':
#                 tmp_answer += n_list[j+1]
#             elif e[j] == '-':
#                 tmp_answer -= n_list[j+1]
#             elif e[j] == '*':
#                 tmp_answer *= n_list[j+1]
#             elif e[j] == '/':    
#                 tmp_answer = int(tmp_answer/n_list[j+1])    # 음수에도 0에 가깝게 나눗셈 위해
                
#         answer.append(tmp_answer)
    
#     print(max(answer))
#     print(min(answer))