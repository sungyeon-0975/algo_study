import sys
# input = sys.stdin.readline
sys.stdin = open('input_1094.txt')

'''
29200KB / 76ms
'''


T = int(input())
for _ in range(T):
    X = int(input())
    stick = (1 << 6)
    stack = [stick]
    while sum(stack) > X:
        temp = stack.pop()
        stack.append((temp >> 1))
        if sum(stack) <= X:
            stack.append((temp >> 1))
    print(len(stack) - stack.count(0))