from collections import deque

DR = [-1, 0, 1, 0]          # 델타 탐색
DC = [0, 1, 0, -1]

def bfs(i, j, place):              # 시작 좌표, 현재 방의 정보
    visited = [[0]*5 for _ in range(5)]     # 방문 처리위한 초기화
    visited[i][j] = 1

    q = deque([(i, j)])                     # 시작 좌표부터 BFS 시작

    while q:
        y, x = q.popleft()      # 현 위치
        for k in range(4):  
            r = y + DR[k]       # 다음 좌표
            c = x + DC[k]

            if 0 <= r < 5 and 0 <= c < 5 and not visited[r][c] and place[r][c] != 'X':  # 범위 안에 있고, 방문하지 않았고, 벽이 아니면
                distance = visited[y][x] + 1                # 첫 시작점으로부터 얼마나 떨어져있는지 계산
                if place[r][c] == 'P' and distance <= 3:    # 거리 차이가 2 이하이고 사람이 있는 경우에
                    return 0                                # 0 반환
                elif distance <= 2:                         # 현재 위치가 시작점으로부터 거리가 1이하인 경우에만 추가적인 탐색위해 값 추가
                    visited[r][c] = distance
                    q.append((r, c))

    return 1


def solution(places):
    answer = []
    
    for place in places:                        # 방별로 순환
        case_ans = []                           # 케이스별 정답을 담아둠

        cnt = 0                                 # 사람의 수 카운트
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':                      # 현재 위치가 사람이면
                    cnt += 1                                # 사람 수 증가
                    case_ans.append(bfs(i, j, place))       # 현재 위치 사람으로부터 2 이하로 떨어진 거리 탐색
        
        if sum(case_ans) == cnt:        # 모든 사람들이 2 초과해서 떨어진 경우에
            answer.append(1)            # 정답에 1 추가
        else:
            answer.append(0)            # 아니면 정답에 0 추가

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))