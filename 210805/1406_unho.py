import sys


'''
use 2 stack
stack1 - string
stack2 - extra



* 알게된 점 *
처음에 리스트로 구현하는거보다 문자열 슬라이싱이 더 빠르다 생각하여 문자열 슬라이싱 사용하였으나 시간 초과
리스트의 pop() append() 가 o(1) 이므로 슬라이싱 하는것보다 더 빠르게 연산할 수 있다.
'''



string = list(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline())
extra = []

for _ in range(num):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == 'L' and string != []:
        extra.append(string.pop())
    elif command[0] == 'D' and extra != []:
        string.append(extra.pop())
    elif command[0] == 'B' and string != []:
        string.pop()
    elif command[0] == 'P':
        string.append(command[1])

while extra:
    string.append(extra.pop())

print(''.join(string))