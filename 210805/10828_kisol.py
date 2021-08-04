import sys
input = sys.stdin.readline

T = int(input())
stack = []

for t in range(T):
    act = input().rstrip()
    if 'push' in act:
        stack.append(int(act[5:]))
    elif act == 'pop':
        if not stack:
            print(-1)
            continue
        print(stack.pop())
    elif act == 'size':
        print(len(stack))
    elif act == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif act == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])