import sys
sys.stdin = open('input.txt')


N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

l, r = 0, 0
answer = []

while l < len(A) and r < len(B):
    if A[l] < B[r]:
        answer.append(A[l])
        l += 1
    else:
        answer.append(B[r])
        r += 1

if l == len(A):
    answer += B[r:]
else:
    answer += A[l:]

print(*answer)