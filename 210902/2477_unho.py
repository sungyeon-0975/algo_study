import sys
sys.stdin = open('input_2477.txt')

K = int(input())

total = 1
len_list = [[] for _ in range(5)]
for i in range(6):
    direction, length = map(int, input().split())