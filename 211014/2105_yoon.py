# import sys
# sys.stdin = open('input.txt')

dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def dfs(i, j, d):
    global ans, stack, path

    if (i, j) == start and len(stack) > 3:
        ans = max(ans, len(stack))
        return

    for (di, dj) in dir:
        if (di, dj) not in path:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] not in stack:
                visited[ni][nj] = 1
                stack.append(arr[ni][nj])
                if d != (di, dj):
                    path.add(d)
                    dfs(ni, nj, (di, dj))
                    path.remove(d)
                else:
                    dfs(ni, nj, d)
                visited[ni][nj] = 0
                stack.pop()

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    stack, path = [], set()
    ans = -1

    for i in range(N-2):
        for j in range(1, N-1):
            start = (i, j)
            dfs(i, j, (1, 1))

    print('#{} {}'.format(t, ans))