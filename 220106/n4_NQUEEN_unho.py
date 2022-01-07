from pprint import pprint

dr = [-1, -1, 1, 1]     # 왼쪽 위, 오른쪽 위, 오른쪽 아래, 왼쪽 아래
dc = [-1, 1, 1, -1]


def DFS(y, x, N, board, coordinates):               # 좌표, 배열의 크기, 보드판, Queen 을 놓은 위치
    visited = [[0] * N for _ in range(N)]           # 방문 여부 체크할 리스트
    stack = [(y, x)]                                # 스택 (시작 좌표)

    while stack:
        node = stack.pop()
        if not visited[node[0]][node[1]]:
            visited[node[0]][node[1]] = 1
            for k in board[node[0]][node[1]]:       # 이동해야하는 방향으로
                r = node[0] + dr[k]
                c = node[1] + dc[k]

                if 0 <= r < N and 0 <= c < N and not visited[r][c] and (r, c) not in coordinates:   # 퀸을 놓치 않았고, 확인해보지 않은 좌표일때
                    stack.append((r, c))                # 스택에 추가하여 확인
                elif (r, c) in coordinates:             # 이동할 곳에 이미 퀸을 놓았으면 False 반환하며 종료
                    return False
    else:                                               # 대각선 상에 퀸이 없으므로 True 반환
        return True


def brute(n, N, board, col_selected, coordinates):               # 현재 행 번호, 보드판 전체 크기, 보드판, 선택된 열 여부 판단 리스트
    global answer

    if n >= N:              # 모든 행 확인 완료하면 정답 개수 추가
        answer += 1
        return

    for c in range(N):
        if not col_selected[c]:                                     # 퀸을 놓지 않은 열일 경우
            col_selected[c] = 1

            if DFS(n, c, N, board, coordinates):                    # 대각선을 탐색하여 대각선상에 퀸이 놓여있지 않으면 실행
                coordinates.add((n, c))                             # 퀸을 놓은 좌표값 추가
                brute(n+1, N, board, col_selected, coordinates)     # 다음 행 재귀 탐색
                coordinates.remove((n, c))                          # 퀸을 놓은 좌표값 삭제
    
            col_selected[c] = 0
    

def solution(grid: list):
    global answer

    N = len(grid)                                               # 주어진 그리드의 길이
    board = [[[] for _ in range(N+1)] for _ in range(N+1)]      # 각 좌표에서 대각선의 방향을 저장하는 리스트
    col_selected = [0] * (N+1)                                  # 열 선택 여부
    coordinates = set()                                         # 퀸을 놓은 좌표값을 저장할 변수
    answer = 0                                                  # 정답 개수

    for i in range(1, N+1):
        for j in range(1, N+1):
            if grid[i-1][j-1] == '0':                           # 주어진 대각선 방향이 정방향일때
                board[i-1][j-1].append(2)                       # 보드판 연결 좌표에 대각선 방향 추가
                board[i][j].append(0)
            
            elif grid[i-1][j-1] == '1':                         # 주어진 대각선 방향이 역방향일때
                board[i-1][j].append(3)                         # 보드판 연결 좌표에 대각선 방향 추가
                board[i][j-1].append(1)

    brute(0, N+1, board, col_selected, coordinates)             # 완전 탐색 시작

    return answer


print(solution(['0010', '0121', '1101', '2000']))
print(solution(['10', '01']))
# TEST
print(f"ex_case : 1 => {solution(['0010121', '1101210', '0102010', '0210201', '0102010', '0122110', '0001112'])}")
print(f"ex_case : 2 => {solution(['000012', '102201', '112201', '112201', '112121', '111111'])}")
print(f"ex_case : 3 => {solution(['000012', '111201', '111111', '100201', '110001', '122011'])}")
print(f"ex_case : 4 => {solution(['00000', '11111', '01020', '11220', '11111'])}")
print(f"ex_case : 5 => {solution(['000', '111', '020'])}")