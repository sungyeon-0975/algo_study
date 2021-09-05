from itertools import permutations          # 순열 모듈
import sys
input = sys.stdin.readline
# 입력
N = int(input())    # 수의 갯수
N_list = list(map(int, input().split()))        # 숫자 리스트
operation = list(map(int, input().split()))     # 연산자 리스트

#연산자 갯수 합
operation_sum = operation[0] + operation[1] + operation[2] + operation[3]

case = 1    # 연산자 총 경우의 수
for o in range(operation_sum, 1, -1):
    case *= o

oper = []   # +, -, *, // 각 갯수만큼 채워넣은 리스트
oper += ['+'] * operation[0]
oper += ['-'] * operation[1]
oper += ['*'] * operation[2]
oper += ['//'] * operation[3]

oper_permu = permutations(oper,len(oper))   # 순열 리스트


result_min = 1e9    # 최소 결과 값을 크게 만듦
result_max = -1e9   # 최대 결과 값을 작게 만듦
for o in oper_permu:                # 순열 리스트를 하나씩 조회
    result = N_list[0]              # result에 첫 번째 숫자를 담음
    for i in range(len(o)):         # 리스트 하나의 길이 만큼 순회
        flag = 0                    # flag 변수 설정
        if o[i] == '+':             # 현재 원소가 + 이면
            result += N_list[i + 1] # result에 다음 숫자를 더함
        elif o[i] == '-':           # 현재 원소가 - 이면
            result -= N_list[i + 1] # result에 다음 숫자를 뺌
        elif o[i] == '*':           # 현재 원소가 * 이면
            result *= N_list[i + 1] # result에 다음 숫자를 곱함
        elif o[i] == '//':          # 현재 원소가 // 이면
            if result * N_list[i + 1] < 0:  # result와 다음 숫자의 곱이 음수이면
                result = -result    # result에 -를 붙임
                flag = 1            # flag를 1로 만듦 (추후 다시 - 붙이기 위함)
            result //= N_list[i + 1]        # result에 다음 숫자를 더함
            if flag == 1:           # flag가 1이면
                result = -result    # result에 -를 붙임

    if result_min > result:         # result가 result_min보다 작으면
        result_min = result         # result_min을 result로 바꿈
    if result_max < result:         # result가 result_max보다 크면
        result_max = result         # result_max를 result로 바꿈

print(result_max)
print(result_min)