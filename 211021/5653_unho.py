import sys
sys.stdin = open('5653_input.txt')


dr = [-1, 0, 1 ,0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N, M, K = map(int, input().split())                                     # height / width / hour
    initial_cell = [list(map(int, input().split())) for _ in range(N)]      # initial cell info

    time_chk = [i for i in range(11)]       # 세포들 시간대별 남은 생명력
    active = [0 for _ in range(11)]         # 세포들 활성상태의 개수 카운트 (각 인덱스가 활성에서 죽을때까지 남은 시간)
    info = [[] for _ in range(11)]          # 각 생명력의 세포들의 비활성 좌표값들
    visited = {}                            # 좌표 방문 여부 (y, x): 0/1
    tc_answer = 0

    for i in range(N):                      # Search cells and coordinate
        for j in range(M):
            if initial_cell[i][j]:
                visited[(i, j)] = 1
                info[initial_cell[i][j]].append((i, j))


    while K != 0:
        print(time_chk)
        for idx in range(10, 0, -1):                    # 동시에 번식시 생명력이 높은게 우선 되어야 하므로 뒤에서 부터 순회
            if not time_chk[idx]:                       # 번식 시기일때
                active[idx] += len(info[idx])
                tmp = info[idx][:]
                info[idx].clear()
                for e in tmp:                           # 각 생명력들 좌표값을 불러옴
                    for k in range(4):
                        r = e[0] + dr[k]                # 새로운 번식 좌표
                        c = e[1] + dc[k]

                        if not visited.get((r, c)):     # 해당 좌표에 아무것도 없을때
                            visited[(r, c)] = 1         # 방문 처리
                            info[idx].append((r, c))    # 새로운 좌표 추가

                time_chk[idx] = idx

            else:                   # 번식 아닐때
                time_chk[idx] -= 1
                
        for idx in range(1, 11):
            active[idx-1] = active[idx]
        active[10] = 0


        K -= 1

    for i in range(10):
        tc_answer += len(info[i+1])

    answer.append('#{} {}'.format(tc, tc_answer+sum(active[1:])))

print(*answer, sep='\n')