import sys

# 57112KB / 376ms
# input = sys.stdin.readline
'''

'''
sys.stdin = open('input_1749.txt')

def find_max_sum():
    global res
    for x1 in range(1, N + 1):
        for y1 in range(1, M + 1):
            for x2 in range(x1, N + 1):
                for y2 in range(y1, M + 1):
                    temp = arr[x2][y2] - arr[x2][y1 - 1] - arr[x1 - 1][y2] + arr[x1 - 1][y1 - 1]
                    if temp > res:
                        res = temp


N, M = map(int, input().split()) # 행, 열
arr = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
res = -987654321

for row in range(1, N+1):
    for col in range(1, M+1):
        arr[row][col] += arr[row][col-1]

for col in range(1, M+1):
    for row in range(1, N+1):
        arr[row][col] += arr[row-1][col]

find_max_sum()
print(res)