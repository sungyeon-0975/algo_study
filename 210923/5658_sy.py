import sys
sys.stdin = open('input/5658_input.txt')

t = int(input())
for idx in range(1,t+1):
    res = set()
    n,k = map(int, input().split())
    s = input()*2
    length = n//4
    for e in range(length, n + length):
        res.add(int(s[e-length:e], 16))
    res = sorted(list(res), reverse=True)[k-1]

    print('#{} {}'.format(idx, res))


