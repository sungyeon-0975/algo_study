import sys
from itertools import combinations

# 60,288KB / 202ms
# input = sys.stdin.readline
'''
각 문제의 배점은 문제마다 다를 수 있고, 틀리면 0점 맞으면 배점만큼의 점수를 받게 된다.
학생들이 받을 수 있는 점수의 경우의 수를 출력
'''
sys.stdin = open('input_3752.txt')

def dfs(n):

    if n == len(problems):
        return

    num = problems[n]
    len_sums = len(sums)
    for i in range(len_sums):
        new_sum = sums[i] + num
        if not scores[new_sum]:
            scores[new_sum] = 1
            sums.append(new_sum)
    dfs(n + 1)

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # N: 문제의 개수
    problems = list(map(int, input().split()))
    scores = [1] + [0] * sum(problems)
    sums = [0]

    dfs(0)

    print('#{} {}'.format(t, len(sums)))


