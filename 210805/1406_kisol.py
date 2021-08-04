import sys, time
start = time.time()
# input = sys.stdin.readline

# chars = []
# chars.extend(input().rstrip())
# T = int(input())
# cursor = len(chars)

# for _ in range(T):
#     act = input().rstrip()
#     if cursor == len(chars) and act == 'D':
#         continue
#     if cursor == 0 and (act == 'L' or act == 'B'):
#         continue
    
#     if act == 'L':
#         cursor -= 1
#     elif act == 'D':
#         cursor += 1
#     elif act == 'B':
#         del chars[cursor - 1]
#         cursor -= 1
#     else:
#         chars.insert(cursor, act[-1])
#         cursor += 1
    
# print(''.join(chars))
lstack = list(sys.stdin.readline().strip())
rstack = []

N = int(input())

for _ in range(N):
    cmd = sys.stdin.readline()
    if cmd[0] == 'L': 
        if lstack:
            rstack.append(lstack.pop())
    elif cmd[0] == 'D': 
        if rstack:
            lstack.append(rstack.pop())
    elif cmd[0] == 'B': 
        if lstack:
            lstack.pop()
    else:
        lstack.append(cmd[2])

print(''.join(lstack + rstack[::-1]))

print(time.time() - start)