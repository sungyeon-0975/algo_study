import sys
sys.stdin = open('21318_input.txt')
# input = sys.stdin.readline

# 41096KB / 284ms

N = int(input())
diff = [0] + list(map(int, input().split()))
pos = [0] * (N+1)
for i in range(1, N+1):
    pos[i] += pos[i-1]
    if diff[i] < diff[i-1]:
        pos[i] += 1
# print(pos)
Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print(pos[y] - pos[x])