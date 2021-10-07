""" 
Memory - 59,724 KB
Time - 222 ms
"""

import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_li = list(map(int, input().split()))
    answer_li = [1] + ([0] * sum(num_li))

    start_idx = 0                           # 현재 가능한 가장 큰 수 (반복횟수 줄이기 위함)
    for e in num_li:
        idx = start_idx
        while idx >= 0:                     # 인덱스가 0번 까지
            if answer_li[idx]:              # 가능한 점수이면
                answer_li[idx+e] = 1        # 그 점수에 현재 점수를 더한것을 가능하게 표시
                if idx + e > start_idx:     # 가장 큰수가 변경되면
                    start_idx = idx + e
            idx -= 1
        
            
    answer = sum(answer_li)

    print('#{} {}'.format(tc, answer))
    


print('-----')



"""
비트마스킹
"""

import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n_li = list(map(int, input().split()))
    a = 1

    for i in n_li:
        a |= a << i
    
    print('#{} {}'.format(tc, bin(a).count('1')))







    # for k in range(N+1):
    #     collect = set(combinations(n_li, k))
    #     # print('LOG --- TC : {} ___ COLLECT : {}'.format(tc, collect))

    #     for element in collect:
    #         answer.add(sum(element))