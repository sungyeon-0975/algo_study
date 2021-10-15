import sys
sys.stdin = open('5653_input.txt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    # 모든 칸 1일때 최대 앞뒤로 K 만큼씩 생성 가능
    cell = [[0] * (M + 2*K) for _ in range(K)] + [[0] * K + list(map(int, input().split())) + [0] * K for _ in range(N)] + [[0] * (M + 2*K) for _ in range(K)]
    active = [0] + [[] for _ in range(10)] # 활성화 세포 (생명력 기준)

    for i in range(N):
        for j in range(M):
            if cell[K+i][K+j]:
                active[cell[K+i][K+j]].append([K+i, K+j, cell[K+i][K+j]]) # [행, 열, 번식 시작까지 대기시간]

    for _ in range(K):
        for vp in range(10, 0, -1): # 생명력 큰 순으로 번식
            cult = active[vp]
            new = []
            kill = []
            for i in range(len(cult)-1, -1, -1): # 뒤에서부터 봐야 pop 가능
                cult[i][2] -= 1
                r, c, w = cult[i]
                if w == -1: # 대기시간 끝나고 번식 시작
                    for k in range(4):
                        nr = r + di[k]
                        nc = c + dj[k]
                        if not cell[nr][nc]:
                            cell[nr][nc] = vp
                            new.append([nr, nc, vp])
                if w == -vp: # 죽일 리스트에 추가
                    kill.append(i)
            for d in kill: # 죽이기
                cult.pop(d)
            cult += new # 새 세포들 추가

    ans = 0
    for idx in range(1, 11):
        ans += len(active[idx])

    print('#{} {}'.format(t, ans))