import sys
from itertools import permutations
# input = sys.stdin.readline
sys.stdin = open('input_14888.txt')

'''
34576KB / 672ms
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    oper_cnt = list(map(int, input().split())) # +-x//
    operator = ['+', '-', '*', '//']
    p = []

    for i in range(4):
        for j in range(oper_cnt[i]):
            p.append(operator[i])

    oper = list(set(permutations(p)))

    ans = []
    for o in oper:
        cal = num[0]
        for n in range(N-1):
            if o[n] == '+':
                cal += num[n+1]
            elif o[n] == '-':
                cal -= num[n+1]
            elif o[n] == '*':
                cal *= num[n+1]
            else:
                if cal < 0:
                    cal = -(abs(cal)//num[n+1])
                else:
                    cal //= num[n+1]
        ans.append(cal)

    print(max(ans))
    print(min(ans))