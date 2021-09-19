import sys
from itertools import combinations
sys.stdin = open('input_4012.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    answer = 1e10

    for one in set(combinations(range(N), N//2)):
        two = set(range(N)) - set(one)

        tmp_one = 0
        for e in combinations(one, 2):
            tmp_one += S[e[0]][e[1]]
            tmp_one += S[e[1]][e[0]]

        tmp_two = 0 
        for e in combinations(two, 2):
            tmp_two += S[e[0]][e[1]]
            tmp_two += S[e[1]][e[0]]

        tmp_answer = abs(tmp_one - tmp_two)
        
        if tmp_answer < answer:
            answer = tmp_answer
    
    print('#{} {}'.format(tc, answer))