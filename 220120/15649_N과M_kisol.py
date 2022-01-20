import sys
# KB / 228ms
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_15649.txt')

def dfs(idx):

    if idx == M:
        print(*sel)
        return  # 필수

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            sel[idx] = arr[i]
            dfs(idx + 1)
            sel[idx] = 0
            visited[i] = 0

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(range(1, N + 1))
    visited = [0] * N
    sel = [0] * M

    dfs(0)