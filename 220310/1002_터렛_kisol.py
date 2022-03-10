import sys
import math

# KB / 72ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_1002.txt')

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if d == 0:
        if r1 != r2: print(0)
        else: print(-1)
    elif abs(r1 - r2) < d < r1 + r2: print(2)
    elif d == abs(r1 - r2) or d == r1 + r2: print(1)
    else: print(0)