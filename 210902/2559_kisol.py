import sys
#input = sys.stdin.readline
sys.stdin = open('input_2559.txt')

N, K = map(int, input().split())
nums = list(map(int, input().split()))
max_sum = sum(nums[:K])
temp_sum = sum(nums[:K])

for i in range(N - K):
    temp_sum += nums[K + i] - nums[i]
    if max_sum < temp_sum:
        max_sum = temp_sum

print(max_sum)