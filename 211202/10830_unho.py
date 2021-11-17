"""
Python
    Memory - 29 MB
    Time - 0.076 s
"""

import sys
sys.stdin = open('input.txt')


def mod(arr):                       # 행렬의 각 값들을 1000으로 나눈 나머지를 구하는 함수
    for i in range(N):
        for j in range(N):
            arr[i][j] %= 1000       # 각 값들을 1000으로 나눈 나머지
    return arr                      # 결과 행렬 반환


def divide_conquer(x):                  # 행렬의 x 제곱의 값을 구하는 함수
    if x < 2:                           # 지수가 2보다 작으면 행렬 반환
        return matrix
    
    arr = divide_conquer(x//2)              # 지수를 2로 나누어서 반환 받음
    result = [[0]*N for _ in range(N)]      # 연산된 결과 행렬
    for i in range(N):                      # 행렬 곱 연산      
        for j in range(N):
            for k in range(N):
                result[i][j] += arr[i][k] * arr[k][j]   

    if x%2:                                     # 지수가 홀수인 경우
        one = divide_conquer(1)                 # 지수가 1인 행렬을 추가적으로 곱함
        result2 = [[0]*N for _ in range(N)]     # 결과 행렬
        for i in range(N):                      # 행렬 곱 연산 / 기존 result 사용시 곱 연산 중 데이터 변형이 생김
            for j in range(N):
                for k in range(N):
                    result2[i][j] += result[i][k] * one[k][j]
        return mod(result2)                     # 행렬의 각 값에서 1000으로 나눈 나머지를 적용하여 행렬 반환
    return mod(result)


N, B = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = mod(divide_conquer(B))         # 초기에 값이 1000이 들어올수 있어 마지막 반환된 값에서 1000으로 나누어줌
for i in range(N):                      # 출력
    print(*answer[i])