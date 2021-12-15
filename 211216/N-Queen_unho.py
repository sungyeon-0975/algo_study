dr = [1, 1, 1]     # 좌하, 우하, 하
dc = [-1, 1, 0]

def chk(y, x, visited, n, direction, num):          # 퀸의 영역 체크
    r = y + dr[direction]                           # 좌표, 방문 변수, 보드판 크기, 진행 방향, 퀸 번호
    c = x + dc[direction]

    if 0 <= r < n and 0 <= c < n:                   
        if not visited[r][c]:                       # 아직 범위 안닿아 있는곳이면 퀸 영역으로 체크
            visited[r][c] = num
        elif visited[r][c] == num:                  # 현재 퀸의 영역이였으면, 영역 삭제
            visited[r][c] = 0
        chk(r, c, visited, n, direction, num)       # 다음 칸


def dfs(row, n, visited, num):                      # 행, 보드판 크기, 방문 변수, 퀸의 번호
    global answer

    if row >= n:                                    # 행 다 돌았으면 정답 추가
        answer += 1
        return

    for col in range(n):                            
        if not visited[row][col]:                   # 현재 행과 열이 퀸의 영역이 닿지 않는 곳이면
            visited[row][col] = num                 # 현재 퀸의 번호로 방문 처리
            for d in range(3):                      # 아래 행에 퀸의 영역으로 방문 처리
                chk(row, col, visited, n, d, num)
                
            dfs(row+1, n, visited, num+1)           # 다음 행 탐색
            
            visited[row][col] = 0                   # 현재 퀸의 번호 영역 삭제
            for d in range(3):                      # 아래 행의 현재 퀸 영역 삭제
                chk(row, col, visited, n, d, num)


def solution(n):
    global answer

    answer = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    dfs(0, n, visited, 1)

    return answer

print(solution(12))




"""
1차 방법
퀸을 노는 자리에 대각선 직선을 모두 검사하여 겹치는거 없는지 확인
검사하는 로직이 너무 많아서 시간 초과 발생
=> 처음에 퀸을 놓으면 대각선 직선으로 모두 방문처리를 시켜버리기
"""
# dr = [-1, -1, 1, 1, -1, 0, 1, 0]     # 좌상, 우상, 좌하, 우하, 상, 우, 하, 좌
# dc = [-1, 1, -1, 1, 0, 1, 0, -1]

# def chk(y, x, visited, n, direction):
#     r = y + dr[direction]
#     c = x + dc[direction]

#     if 0 <= r < n and 0 <= c < n:
#         if visited[r][c]:
#            return False
#         return chk(r, c, visited, n, direction)
#     return True


# def dfs(row, n, visited):
#     global answer

#     if row >= n:
#         answer += 1
#         return

#     for col in range(n):
#         if not visited[row][col]:
#             for d in range(8):
#                 if not chk(row, col, visited, n, d):
#                     break
#             else:
#                 visited[row][col] = 1
#                 dfs(row+1, n, visited)
#                 visited[row][col] = 0


# def solution(n):
#     global answer

#     answer = 0
#     visited = [[0 for _ in range(n)] for _ in range(n)]

#     dfs(0, n, visited)

#     return answer

# print(solution(4))