import sys
sys.setrecursionlimit(10**9)
# 37864KB / 1628ms
# input = sys.stdin.readline
'''
런타임에러 재귀문제
'''

sys.stdin = open('input_2468.txt')

def dfs(r, c):
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc] and arr[nr][nc] > h:
                visited[nr][nc] = 1
                dfs(nr, nc)

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_h = min(sum(arr, []))
    max_h = max(sum(arr, []))
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    max_cnt = 1

    for h in range(min_h, max_h):
        visited = [[0] * N for _ in range(N)]
        cnt = 0
        for r in range(N):
            for c in range(N):
                if arr[r][c] > h and not visited[r][c]:
                    dfs(r, c)
                    cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)