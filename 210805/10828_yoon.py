import sys
input = sys.stdin.readline

N = int(input())
stack = [] # 스택이란 거 마지막에 넣은 게 위에 있는 거라고 왜 아무도 말 안해줬어? 그야 물어보질 않았으니까요

for n in range(N):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)