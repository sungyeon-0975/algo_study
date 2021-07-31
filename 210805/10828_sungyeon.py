import sys 
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    stack = []
    for _ in range(n):
        command = input().strip()
        if command.startswith('push'):
            stack.append(command[5:].strip())
        elif command =='pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command == 'size':
            print(len(stack))
        elif  command == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        else:# top
            if stack:
                print(stack[-1])
            else:
                print(-1)
