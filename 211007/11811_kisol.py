import sys

# 29200KB / 316ms (sys 포함할 경우 줄어듦)
# input = sys.stdin.readline
'''
크기 N의 정사각 행렬이 있는데, i번째 행 j번째 열에 적힌 숫자는 ai와 aj에 비트연산 and를 수행한 결과값이다.
a1~aN을 구하여 출력
POINT) 여러 가지 답이 있다는 거!! 예시 출력에 매몰되면 안 되는 문제였음. 
'''
sys.stdin = open('input_11811.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    result = [0] * N
    for i in range(N):
        arr = list(map(int, input().split()))
        a = 0
        for num in arr:
            a |= num
        result[i] = a

    print(*result)  # POINT) 출력할 때 맨 마지막 공백도 확인 필수
