import sys
import bisect
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                               # 수열의 길이
A = list(map(int, sys.stdin.readline().split()))            # 수열
lis = [0]                                                   # 최장 증가 부분 수열(LIS)

for num in A:                                               # 수열 하나씩 확인
    if num > lis[-1]:                                       # LIS의 가장 우측 리스트의 값 보다 현재 값이 더 크면
        lis.append(num)                                     # LIS에 값 추가
    else:
        lis[bisect.bisect_left(lis, num, lo=1)] = num       # 현재 숫자가 LIS 변수에 들어갈 위치 찾기

print(len(lis)-1)