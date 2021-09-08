'''
실행시간 : 76ms
(import sys 한거랑 안한거랑 동일 -> readline하면 strip해야해서 그런거일수도??)
'''
import sys
input = sys.stdin.readline

def number_sum(s):
    res = 0
    for i in s:
        if i.isdigit():
            res += int(i)
    return res


if __name__ == "__main__":
    n = int(input())
    l = [input().strip() for _ in range(n)]

    print('\n'.join(sorted(l, key = lambda x: (len(x),number_sum(x), x))))