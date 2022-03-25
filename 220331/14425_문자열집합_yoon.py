from collections import defaultdict
import sys
sys.stdin = open('14425_input.txt')
# input = sys.stdin.readline

# 38040KB / 184ms

N, M = map(int, input().split())
S = defaultdict(int)
ans = 0
for _ in range(N):
    w1 = input().strip()
    S[w1] += 1
for _ in range(M):
    w2 = input().strip()
    if S[w2] > 0:
        ans += 1
print(ans)