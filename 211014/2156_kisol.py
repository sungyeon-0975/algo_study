import sys

# KB / ms
# input = sys.stdin.readline
'''
'''
sys.stdin = open('input_2156.txt')


n = int(input())
array = [0] * n
for i in range(n):
    array[i] = int(input())

d = [0] * n
d[0] = array[0]
d[1] = array[0] + array[1]
d[2] = max(array[2] + array[0], array[2] + array[1], d[1])
for i in range(3, n):
    d[i] = max(array[i] + d[i - 2], array[i] + array[i - 1] + d[i - 3], d[i - 1])

print(max(d))
