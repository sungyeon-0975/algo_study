'''
itertools 활용
Memory - 35088 KB
Time - 656 ms

recursion 활용해서 해볼 필요 있음
'''


import sys
import itertools
sys.stdin = open('input_14888.txt')

test_case = int(input())

for _ in range(test_case):
    N = int(input())
    n_list = list(map(int, input().split()))    # 숫자 리스트
    operator = list(map(int, input().split()))  # 연산자 리스트 (덧셈 / 뺄셈 / 곱셈 / 나눗셈)
    op = []

    for idx in range(4):                        # 연산자들을 리스트 리스트로
        if idx == 0:
            c = '+'
        elif idx == 1:
            c = '-'
        elif idx == 2:
            c = '*'
        elif idx == 3:
            c = '/'
        
        op.extend(c*operator[idx])

    permu = set(itertools.permutations(op, len(op)))    # 순열 구함, 중복 제거

    answer = []
    for e in permu:                                     # 앞에서부터 계산
        tmp_answer = n_list[0]
        for j in range(len(e)):
            if e[j] == '+':
                tmp_answer += n_list[j+1]
            elif e[j] == '-':
                tmp_answer -= n_list[j+1]
            elif e[j] == '*':
                tmp_answer *= n_list[j+1]
            elif e[j] == '/':    
                tmp_answer = int(tmp_answer/n_list[j+1])    # 음수에도 0에 가깝게 나눗셈 위해
                
        answer.append(tmp_answer)
    
    print(max(answer))
    print(min(answer))