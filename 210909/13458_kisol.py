import sys
from math import ceil
# 155708 KB / 644 ms

# input = sys.stdin.readline
sys.stdin = open('input_13458.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    supervisor = N  # 총감독관(B)은 무조건 반마다 1명씩 있기 때문에

    for a in A:
        a -= B  # 총감독관(B)가 맡을 수 있는 학생수 빼주기
        if a > 0:  # 만약 빼주고도 남을 경우
            supervisor += ceil(a / C)  # 부감독관(C)가 맡을 수 있는 학생수로 나누고 올림처리
    print(supervisor)
