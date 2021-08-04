import sys
input = sys.stdin.readline

if __name__ == "__main__":
    stack1 = list(input().strip())
    stack2 = []
    n = int(input())
    for _ in range(n):
        command = input()
        if command[0] == 'L':
            if stack1:
                stack2.append(stack1.pop())
        elif command[0] == 'D':
            if stack2:
                stack1.append(stack2.pop())
        elif command[0] == 'B':
            if stack1:
                stack1.pop()
        else:# P
            stack1.append(command[2])
    print(''.join(stack1 + list(reversed(stack2))))



 