import sys
sys.stdin = open('input/4014_input.txt')


def check(i):
    j = 1
    c = 1
    while j < n:
        diff = l[i][j] - l[i][j-1]
        if diff == 0:
            c += 1
        elif diff == -1 and c >= 0:
            c = 1 - x
        elif diff == 1 and c >=  x:
            c = 1
        else:
            return 0
        j += 1

    if c >= 0:
        return 1
    else:
        return 0

t = int(input())
for idx in range(1, t+1):
    n, x = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    l += list(zip(*l))
    res = 0
    for i in range(2*n):
        res += check(i)

    print('#{} {}'.format(idx, res))