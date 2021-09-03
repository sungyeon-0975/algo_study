import sys

sys.stdin = open('input_2309.txt')
# 순열은 중복이 있다
from itertools import combinations

data = [int(input()) for i in range(9)]

c_data = combinations(data, 7)

answer = []
for i in c_data:
    if sum(i) == 100:
        for j in i:
            answer.append(j)
        break

answer.sort()
for i in answer:
    print(i)
