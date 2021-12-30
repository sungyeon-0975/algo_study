import sys
sys.setrecursionlimit(10**6)
# 40476KB / 3976ms Python3
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_2573.txt')


# 분리 상태 확인
def check_state(r, c):
    global check, cnt
    cnt += 1
    visited[r][c] = 1
    # 방문한 곳의 수가 전체 빙산의 수와 같으면 분리여부 False 처리
    if cnt == pos_len:
        check = False
        return
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if not visited[nr][nc] and arr[nr][nc]:
            check_state(nr, nc)
        if not check:
            return


# 녹이기
def melt():
    idx = 0
    melted_list = []
    # 녹은 후 값 구하기
    while idx < len(positions):
        melt_cnt = 0  # 녹일 수
        r, c = positions[idx][0], positions[idx][1]  # 빙산 위치(행, 열)
        # 4방향 바닷물(0) 여부 체크하여 녹일 수에 추가
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not arr[nr][nc]:
                melt_cnt += 1
        # 녹일 수를 뺐을 때 0 이하면 0, 아니면 그냥 뺀 값
        ice = 0 if arr[r][c] - melt_cnt <= 0 else arr[r][c] - melt_cnt
        melted_list.append((r, c, ice))  # (행, 열, 녹인후 값) append처리
        # 녹인후 값이 0이면 빙산의 위치 리스트에서 제거
        if ice == 0:
            positions.pop(idx)
            idx -= 1
        idx += 1
    # 녹은 후 값으로 바꿔주기
    for r, c, ice in melted_list:
        arr[r][c] = ice


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
years = 0  # 시간(년)
check = False  # 분리 여부
positions = []  # 빙산 위치
dr = [-1, 0, 1, 0]  # 북동남서
dc = [0, 1, 0, -1]

# 빙산 위치 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            positions.append((i, j))

# 분리되지 않았고, 빙산이 남아있는 동안
while not check and positions:
    visited = [[0] * M for _ in range(N)]
    pos_len = len(positions)  # 빙산의 칸 개수
    check = True  # 분리되었다고 생각하고
    cnt = 0
    check_state(positions[0][0], positions[0][1])  # 여기서 분리가 안됐으면 분리여부 False 처리
    if check:  # 분리가 되었으면 break
        break
    melt()  # 분리가 안되었으면 녹인 후 1년 증가
    years += 1

# 분리가 되었으면 걸린 년수 출력
if check:
    print(years)
# 아니면 0 출력
else:
    print(0)
