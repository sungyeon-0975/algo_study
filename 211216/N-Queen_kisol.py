global answer
answer = 0


def solution(n):
    global answer
    visited = [[0] * n for _ in range(n)]
    for i in range(n):  # 맨 첫번째 행중에서 열 하나씩 옮겨가며 dfs 진행
        visited[0][i] = 1
        dfs(1, n, visited, [i])
        visited[0][i] = 0
    return answer


def dfs(r, n, visited, col_list):
    global answer
    if r == n:
        answer += 1
        return
    for c in range(n):
        if c not in col_list:  # 이거 추가하니까 통과!!ㅎㅎ (이미 사용한 열 번호는 제외하고 진행)
            for i in range(r):  # 행 번호
                left_c = c - (r - i)  # 왼쪽 대각선
                right_c = c + (r - i)  # 오른쪽 대각선
                # 왼쪽 대각선이나 오른쪽 대각선 확인했을 때 겹치면 break
                if (0 <= left_c < n and visited[i][left_c]) or (0 <= right_c < n and visited[i][right_c]):
                    break
            else:  # 겹치는게 없는 경우
                visited[r][c] = 1
                dfs(r + 1, n, visited, col_list + [c])  # 사용한 col_list에 추가된 열 번호 추가해서 재귀
                visited[r][c] = 0


print(solution(4))
