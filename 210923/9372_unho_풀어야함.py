import sys
sys.stdin = open('input_9372.txt')


T = int(sys.stdin.readline().split())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    for idx in range(M):
        a, b = map(int, sys.stdin.readline().split())
        