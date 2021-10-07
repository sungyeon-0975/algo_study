"""
31156KB 84ms

논리회로
(~K)+1 은  K의 2의 보수 즉 , -K
K& -K 는 최하위 1인 비트
K = K에서 최하위 1 비트를 제외한 값
즉, 1을 하나씩 빼는 연산을 몇번 할 것인가?
"""

import sys
sys.stdin = open('input_17419.txt')

input()
print(input().count('1'))

