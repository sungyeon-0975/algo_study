import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp_list = list(map(int, input().split()))
temp = sum(temp_list[:K])
result = temp
for i in range(N - K):
    temp = temp - temp_list[i] + temp_list[i+K]
    result = max(result, temp)
print(result)