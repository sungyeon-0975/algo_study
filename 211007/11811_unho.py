"""
Memory - 37004 KB (36.13 MB)
Time - 344 ms
"""


import sys
sys.stdin = open('input.txt')


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = [0] * N

for i in range(N):
    for j in range(i+1, N):
        if arr[i][j] != (answer[i] & answer[j]):        # and 연산이 배열의 값과 다를때
            answer[i] |= arr[i][j]
            answer[j] |= arr[i][j]
print(*answer)