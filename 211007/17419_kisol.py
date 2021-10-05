import sys

# 39596KB / 204ms
# input = sys.stdin.readline
'''

'''
sys.stdin = open('input_17419.txt')


N = int(input())  # 자릿수
K = sum(list(map(int, input())))  # 숫자(2진수)
print(K)  # 1의 개수 = 연산 횟수