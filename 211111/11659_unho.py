import sys


num, time = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0, num_list[0]] # 누적합을 저장해두는 리스트

# 누적합
for idx in range(1, num):
    sum_list.append(sum_list[idx] + num_list[idx])

for _ in range(time):
    start, end = map(int, sys.stdin.readline().split())
    
    print(sum_list[end] - sum_list[start-1])