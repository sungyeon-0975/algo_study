import sys
sys.stdin = open('input.txt')


def solution(y, x):
    stack = [(y, x)]                # DFS 탐색

    while stack:
        node = stack.pop()
        for k in range(8):          # 섬의 주변을 탐색
            r = node[0] + dr[k]
            c = node[1] + dc[k]

            if 0 <= r < H and 0 <= c < W and not visited[r][c] and board[r][c] == 1:    # 땅이면서, 아직 방문하지 않은 섬일때
                visited[r][c] = 1                                                       # 땅 방문 처리 및 다음 탐색을 위한 추가
                stack.append((r, c))



dr = [-1, 0, 1, 0, -1, -1, 1, 1]        # 상 우 하 좌 좌상 우상 좌하 우하
dc = [0, 1, 0, -1, -1, 1, -1, 1]

while True:
    W, H = map(int, sys.stdin.readline().split())       # 너비, 높이

    if W == 0 and H == 0:                               # 테스트케이스 종료
        break

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]    # 섬과 바다 입력
    visited = [[0] * W for _ in range(H)]                                       # 섬을 방문했는지 여부 체크 위한 리스트
    answer = 0                                                                  # 섬의 개수를 카운트 하는 변수

    for i in range(H):                                      # 섬을 돌면서 확인하지 않은 섬을 체크
        for j in range(W):
            if board[i][j] == 1 and not visited[i][j]:      # 땅이면서 아직 확인하지 않은 섬이면
                visited[i][j] = 1                           # 방문처리 및 섬의 개수 추가
                answer += 1
                solution(i, j)

    print(answer)