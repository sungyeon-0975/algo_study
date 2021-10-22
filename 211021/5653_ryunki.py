import sys

sys.stdin = open('5653_input.txt')
"""
활성시 첫 1시간 상하좌우
동시번식 경우에만 생명력이 높은 쪽이 번식
visited에 가운데에 위치시킨 후 반복문을 돌면서 생명력 -=1 하다가
0이 되는 경우는 활성상태니깐 탐색해서 0인 경우에는 양옆을 확인 후 0인 경우에는 번식
겹치는 경우를 해결하기 위해 높은 생명력부터 번식상태라면 번식시킨다
결과적으로 원래 생명력을 알아야 하니깐 Visited에 생명력과 원래 생명력 두개를 추가 (x) 아예 생명력을 따로 저장한 후에 생명력을 큰 순서부터 보는게 나을듯
-해당 생명력이 되는경우에는 죽은 세포 더이상 지켜보지 않는다.
bfs를 사용한다.
"""
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for test in range(1, 1 + int(input())):
    N, M, K = map(int, input().split())
    data = list(list(map(int, input().split())) for _ in range(N))
    visited = [[0] * (M + K) for _ in range(N + K)]  # 전체크기의 맵
    cells = [[] for _ in range(11)]  # 세포마다의 생명력들의 위치

    for i in range(N):
        for j in range(M):
            if data[i][j]:
                visited[i + K // 2][j + K // 2] = data[i][j]  # 생명력 넣기
                cells[data[i][j]].append((i + K // 2, j + K // 2))  # 생명력의 좌표를 따로 저장

    for i in range(1, K + 1): # 시간
        for hp in range(10, 0, -1): # 가장 큰 생명력 부터 번식
            if i % (hp + 1): # 해당 시간과 생명력이 하나 더 작은게 나눠떨어지는 경우 == 번식이 시작된다
                continue
            temp = [] # 살아있는 생명체들
            for j in cells[hp]: # 해당생명력의 좌표들을 돌면서

                if K - i < hp - 1: # ??
                    temp.append(j)

                for dx, dy in move: # 돌면서
                    nx = j[0] + dx
                    ny = j[1] + dy
                    if not visited[nx][ny]: # 갈 수 있는 위치라면
                        visited[nx][ny] = hp # 해당 곳을 해당 생명력으로 갱신
                        temp.append((nx, ny)) # 아직 죽지 않은 생명체들
            cells[hp] = temp # 해당 생명력에 살아있는 생명체들 교체
    answer = 0
    for i in cells:
        answer += len(i)
    print('#{} {}'.format(test, answer))
