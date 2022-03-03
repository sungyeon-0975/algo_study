import sys
# KB / ms
# input = sys.stdin.readline
'''
'''

sys.stdin = open('input_2512.txt')

# 다른 방법
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

total = sum(arr)
max_n = max(arr)

if total <= M:
    print(max_n)
else:
    sub = total - M
    ceiling = max_n - (sub // N)

    while True:
        temp = 0
        for i in range(N):
            if arr[i] > ceiling:
                temp += arr[i] - ceiling
        if temp >= sub:
            break
        ceiling = ceiling - ((sub - temp) // N) if sub - temp >= N else ceiling - 1

    print(ceiling)

# 이분 탐색
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

total = sum(arr)
max_n = max(arr)

if total <= M:
    print(max_n)
else:
    end = max_n
    start = max_n - (total - M)
    ans = 0
    min_sub = max_n

    while start <= end:
        ceiling = (start + end) // 2

        temp = 0
        for i in range(N):
            if arr[i] > ceiling:
                temp += ceiling
            else:
                temp += arr[i]
        sub = M - temp
        if sub >= 0:
            if sub < min_sub:
                ans = ceiling
                min_sub = sub
            start = ceiling + 1
        else:
            end = ceiling - 1

    print(ans)