grid_dr = [-1, 0, 0, -1]  # 우상, 우하, 좌하, 좌상
grid_dc = [0, 0, -1, -1]
arr_dr = [-1, 1, 1, -1] # 우상+1(양의 대각선), 우하+0(음의 대각선), 좌하+1, 좌상+0
arr_dc = [1, 1, -1, -1]

def check_diagon(r, c, grid, visited):
    global flag
    for d in range(4):
        gr, gc = r + grid_dr[d], c + grid_dc[d]
        if 0 <= gr < n - 1 and 0 <= gc < n - 1:
            if (d % 2 == 0 and grid[gr][gc] == '1') or (d % 2 == 1 and grid[gr][gc] == '0'):
                nr, nc = r + arr_dr[d], c + arr_dc[d]
                if 0 <= nr < n and 0 <= nc < n:
                    if not visited[nr][nc]:
                        visited[nr][nc] = 1
                        check_diagon(nr, nc, grid, visited)
                        visited[nr][nc] = 0
                        if flag:
                            return
                    elif visited[nr][nc] == 2:
                        flag = True
                        return


def n_queen(r, n, grid, visited, col_list):
    global answer, flag
    if r == n:
        answer += 1
        return
    for c in range(n):
        if c not in col_list:  # 이미 사용한 열 번호는 제외하고 진행
            flag = False
            visited[r][c] = 1
            check_diagon(r, c, grid, visited)
            visited[r][c] = 0
            if flag == False:
                visited[r][c] = 2
                n_queen(r + 1, n, grid, visited, col_list + [c])  # 사용한 col_list에 추가된 열 번호 추가해서 재귀
                visited[r][c] = 0


def solution(grid):
    global answer, n, flag
    answer = 0
    n = len(grid) + 1
    visited = [[0] * n for _ in range(n)]
    flag = False
    for i in range(n):  # 맨 첫번째 행중에서 열 하나씩 옮겨가며 dfs 진행
        visited[0][i] = 2
        n_queen(1, n, grid, visited, [i])
        visited[0][i] = 0
    return answer


print(solution(["0010", "0121", "1101", "2000"]))
print(solution(["10", "01"]))