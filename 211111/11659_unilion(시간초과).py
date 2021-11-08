import sys
# sys.stdin = open('11659_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
N_tuple = tuple(map(int, input().split()))
for _ in range(M):
    i, j = map(int, input().split())
    result = 0
    for k in range(i - 1, j):
        result += N_tuple[k]
    print(result)