from collections import deque


def solution(maps):
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]

    n, m = len(maps), len(maps[0])
    v = [[0]*m for _ in range(n)]
    v[0][0] = 1
    dq = deque([(0, 0)])

    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] and not v[nr][nc]:
                    if nr == n-1 and nc == m-1:
                        return v[r][c] + 1
                    v[nr][nc] = v[r][c] + 1
                    dq.append((nr, nc))

    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
