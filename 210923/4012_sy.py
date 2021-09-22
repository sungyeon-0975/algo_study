import sys
sys.stdin = open('input/4012_input.txt')
from itertools import combinations

def synergy(comb):
    return sum([l[x[0]][x[1]] for x in  list(combinations(comb, 2))])


t = int(input())
for idx in range(1,t+1):
    n = int(input())
    l = [[0]*n] + [[0] + list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n+1):
        for j in range(i+1,n+1):
            l[i][j] += l[j][i]
    whole = [i for i in range(1, n+1)]
    whole_set = set(whole)
    res = map(lambda x:  abs(synergy(x) - synergy(whole_set - set(x))), combinations(whole, n//2))

    print('#{} {}'.format(idx, min(res)))
    


