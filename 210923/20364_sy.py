'''
실행시간 : 724ms
'''

import sys
input = sys.stdin.readline

def check(idx):
    i = duck[idx]
    val = 0
    while i > 0:
        if occupied[i] == 1:
            val = i
        i //= 2
    if val == 0:
        occupied[duck[idx]] = 1 
    duck[idx] = val

if __name__ == "__main__":
    n, q = map(int, input().split())
    occupied = [0]*(n+1)
    duck = [int(input()) for _ in range(q)]
    for i in range(q):
        check(i)
    
    for i in range(q):
        print(duck[i])