'''
Memory - 155724 KB
Time - 880 ms
'''

import sys
import math
sys.stdin = open('input_13458.txt')

test_case = int(input())

for _ in range(test_case):
    N = int(input())
    A_list = list(map(int, input().split()))
    B, C = map(int, input().split())
    answer = N

    for idx in range(N):
        tmp = A_list[idx] - B
        if tmp > 0:
            answer += int(math.ceil(tmp/C))
    
    print(answer)