import sys

# 39468KB / 304ms
# input = sys.stdin.readline
'''

'''
sys.stdin = open('input_11659.txt')

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

# 누적합 구하기
for idx in range(2, N + 1):
    nums[idx] += nums[idx - 1]

# 구간합 M번 구하기
for _ in range(M):
    i, j = map(int, input().split())
    print(nums[j] - nums[i - 1])