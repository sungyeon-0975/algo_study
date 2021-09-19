""" 
Memory - 50196 KB
Time - 1236 ms
"""


import sys
sys.stdin = open('input_20364.txt')


N, Q = map(int, sys.stdin.readline().split())
land = {}


for _ in range(Q):
    want = int(sys.stdin.readline())
    answer = 0

    idx = want
    while idx >= 2:
        if land.get(idx, False):
            answer = idx
        idx //= 2
    land[want] = True
    
    print(answer)