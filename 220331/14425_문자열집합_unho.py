import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
S = {sys.stdin.readline().rstrip() for _ in range(N)}
query = [sys.stdin.readline().rstrip() for _ in range(M)]
answer = 0

for c in query:
    if c in S:
        answer += 1

print(answer)