import sys


num, time = map(int, sys.stdin.readline().split())          # 수의 개수, 합을 구해야 하는 횟수
num_list = list(map(int, sys.stdin.readline().split()))     # 숫자 리스트
sum_list = [0, num_list[0]]                                 # 누적합을 저장해두는 리스트

# 누적합
for idx in range(1, num):                               # 누적합 구하기
    sum_list.append(sum_list[idx] + num_list[idx])

for _ in range(time):
    start, end = map(int, sys.stdin.readline().split()) # 해당 구간합 구하기
    
    print(sum_list[end] - sum_list[start-1])