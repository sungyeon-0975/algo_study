import sys

# 40236KB / 156ms
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_1806.txt')

N, S = map(int, input().split())
nums = list(map(int, input().split()))

# 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이 구하기
end = 0
temp_sum = 0
res = N + 1  # 찾는다면 길이 N 이상이 나올 수 없기 때문에 판별용
for start in range(N):
    while temp_sum < S and end < N:
        temp_sum += nums[end]
        end += 1

    if temp_sum >= S:
        res = min(res, end - start)
    temp_sum -= nums[start]

if res == N + 1:
    print(0)
else:
    print(res)
