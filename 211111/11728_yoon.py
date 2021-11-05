import sys
sys.stdin = open('11728_input.txt')
# input = sys.stdin.readline

# 184088KB / 2168ms 미친건가

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

new = []
i, j = 0, 0
while i < N and j < M:
    if A[i] < B[j]:
        new.append(A[i])
        i += 1
    else:
        new.append(B[j])
        j += 1
if i < N:
    new.extend(A[i:])
else:
    new.extend(B[j:])
print(*new)