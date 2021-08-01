import sys


'''
##1차 생각
#원리
각 집합의 원소의 값을 집합 형태로 데이터 받는다
각 차집합을 구한 후 합집합 시킨다.

#상세
1. 두 집합을 difference 이용하여 차집합 구한다.
2. 각 차집합을 union 이용하여 합집합을 구한다.
3. 요소의 개수를 구한다.
'''


a_number, b_number = map(int, sys.stdin.readline().split())
a_set = set(map(int, sys.stdin.readline().split()))
b_set = set(map(int, sys.stdin.readline().split()))

# 각 차집합을 구한다.
a_dif = a_set.difference(b_set)
b_dif = b_set.difference(a_set)

# 두 차집합의 합집합을 구한다.
answer = a_dif.union(b_dif)

print(len(answer))