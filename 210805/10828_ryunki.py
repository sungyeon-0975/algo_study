# push x 정수x를 스택에 넣는다
# pop스택에서 가장 위에 있는 정수를 빼고 그수를 출력한다. 없는경우에는 -1출력
# size 스택에 들어있는 정수의 개수 출력
# empty 스택이 비어있으면, 1, 아니면 0을 출력
# top스택의 가장위에 있는 정수를 출력 없는 경우 -1
import sys
N = int(sys.stdin.readline())
stack = []

def push(x):
    return stack.append(x)

def pop():
    if len(stack):
        return print(stack.pop(-1))
    else:
        return print(-1)

def size():
    return print(len(stack))

def empty():
    if len(stack):
        return print(0)
    else:
        return print(1)

def top():
    if len(stack):
        return print(stack[-1])
    else:
        return print(-1)

for i in range(N):    
   
        command = sys.stdin.readline().split()
        if 'push' in command:
            push(command[-1])
        elif 'pop' in command:
            pop()
        elif 'size' in command:
            size()
        elif 'empty' in command:
            empty()
        elif 'top' in command:
            top() 