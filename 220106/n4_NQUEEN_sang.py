def solution(grid):
    ans = 0
    l = len(grid)

    # 연결노드 저장
    def check(r, c):
        mp[r][c] = cnt
        for i in range(4):
            gr, gc = r + dgr[i], c + dgc[i]
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= gr < l and 0 <= gc < l and not mp[nr][nc]:
                if not i % 2 and grid[gr][gc] == '0':
                    check(nr, nc)
                if i % 2 and grid[gr][gc] == '1':
                    check(nr, nc)

    # 완전 탐색
    def dfs(n):
        nonlocal ans
        nonlocal chk

        if n == l+1:
            ans += 1

        for i in range(l+1):
            if not visited[i] and mp[n][i] not in chk:
                visited[i] = (n, i)
                chk.add(mp[n][i])
                dfs(n+1)
                visited[i] = 0
                chk = chk - set([mp[n][i]])

    mp = [[0]*(l+1) for _ in range(l+1)]
    dr, dc = [-1, -1, 1, 1], [-1, 1, 1, -1]
    dgr, dgc = [-1, -1, 0, 0], [-1, 0, 0, -1]
    cnt = 0

    for i in range(l+1):
        for j in range(l+1):
            if not mp[i][j]:
                cnt += 1
                check(i, j)

    visited = [0] * (l+1)
    chk = set()
    dfs(0)

    return ans


print(solution(["0010", "0121", "1101", "2000"]))
print(solution(["10", "01"]))
