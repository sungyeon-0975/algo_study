dr = [0, 1, 1]
dc = [1, 1, 0]


def solution(m, n, board):
    answer = 0
    arr = [[0] * m for _ in range(n)]
    exist = True  # 4개 블록 존재 여부

    # 재배열 (오른쪽으로 90도 회전)
    for j in range(n):
        for i in range(m):
            arr[j][m - i - 1] = board[i][j]

    # 4블록짜리가 존재할 동안
    while exist:
        visited = [[0] * m for _ in range(n)]
        exist = False  # 존재할 때 True 처리할거기 때문에 False 처리
        for r in range(len(arr) - 1):
            for c in range(len(arr[r]) - 1):  # 행마다 길이가 달라짐
                char = arr[r][c]
                stack = []
                for d in range(3):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < len(arr) and 0 <= nc < len(arr[nr]) and arr[nr][nc] == char:
                        stack.append((nr, nc))
                    else:
                        break
                else:  # 만약 3개 다 일치할 경우, stack에서 꺼내서 visited 표시
                    exist = True
                    visited[r][c] = 1
                    while stack:
                        nr, nc = stack.pop()
                        visited[nr][nc] = 1

        # 블록 깨기
        for r in range(n):
            cnt = 0
            for c in range(m):
                if visited[r][c]:  # 방문한 곳이면
                    arr[r].pop(c - cnt)  # pop(방문한곳 열 좌표 - 해당 행에서 깨진 블록 개수)
                    cnt += 1  # 해당 행에서 깨진 블록수 +1
            answer += cnt  # 전체 깨진 블록수 + (해당 행에서 깨진 블록수)

    return answer


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))