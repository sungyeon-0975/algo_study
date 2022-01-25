from collections import deque

dr = [-1, 0, 1, 0]      # 상 우 하 좌
dc = [0, 1, 0, -1]

def solution(maps):
    N = len(maps)                               # 세로
    M = len(maps[0])                            # 가로
    visited = [[0] * M for _ in range(N)]       # 방문 여부

    def solution():                 # 내부함수, BFS 탐색
        q = deque([(0, 0)])
        visited[0][0] = 1           # 시작점 방문 처리

        while q:
            node = q.popleft()
            for k in range(4):          # 다음 새로운 좌표
                r = node[0] + dr[k]
                c = node[1] + dc[k]

                if 0 <= r < N and 0 <= c < M and not visited[r][c] and maps[r][c]:      # 범위 안이고, 아직 방문하지 않은 빈 공간이면
                    visited[r][c] = visited[node[0]][node[1]] + 1                       # 거리 증가해서 방문 체크
                    q.append((r, c))

    solution()

    if visited[N-1][M-1]:               # 도착 지점에 갈 수 있으면 이동 거리 반환
        return visited[N-1][M-1]

    return visited[N-1][M-1] - 1        # 도착 지점에 갈 수 없으면 -1 반환
    

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))