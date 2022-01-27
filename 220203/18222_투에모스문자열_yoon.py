# import sys
# sys.stdin = open('4963_input.txt')
# input = sys.stdin.readline

# 시간초과

k = int(input())
a = '0'
b = ''
while len(a) < k:
    for i in range(len(a)):
        if a[i] == '1':
            b += '0'
        else:
            b += '1'
    a += b
print(a[k-1])