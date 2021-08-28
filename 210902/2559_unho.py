import sys

N, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

answer = tmp_sum = sum(num_list[:K])

idx = K
while idx < N:
    tmp_sum = tmp_sum - num_list[idx-K] + num_list[idx]     # 오른쪽으로 이동하면서 맨왼쪽 빼고, 오른쪽을 더해서 합을 구함

    if tmp_sum > answer:
        answer = tmp_sum
    
    idx += 1

print(answer)