import sys
sys.stdin = open('1806_input.txt')
# input = sys.stdin.readline

# 40236KB / 188ms

N, S = map(int, input().split())
arr = list(map(int, input().split()))
acc = [0] * (N+1)
res = 987654321
for k in range(1, N+1):
    acc[k] = acc[k-1] + arr[k-1]

i, j = 0, 1
while j < N+1:
    if acc[j] - acc[i] >= S:
        res = min(res, j-i)
        i += 1
    else:
        j += 1

if res == 987654321:
    res = 0
print(res)