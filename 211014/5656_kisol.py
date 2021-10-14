import sys
# 504ms
sys.stdin = open('input_5656.txt')


# 되돌리는 함수 (전체 배열 append로 만들어서 주소 복사되지 않음)
def make_arr(bricks):
    arr = [[] for _ in range(W)]
    for i in range(W):
        for j in range(H):
            arr[i].append(bricks[i][j])
    return arr


# 현재 위치한 숫자 기준으로 사방으로 뻗어나가며 -1로 변경하는 함수
def dfs(r, c, num):
    for d in range(4):
        for n in range(1, num):
            nr, nc = r + (dr[d] * n), c + (dc[d] * n)  # 1칸씩 늘릴거기 때문에 n을 곱해줘서 nr, nc 구함. 곱하지 않을시 제자리
            if 0 <= nr < W and 0 <= nc < H:
                n_num = arr[nr][nc]
                if n_num > 1:  # 1보다 큰 경우 -1로 변경 후 dfs로 또 탐색
                    arr[nr][nc] = -1
                    dfs(nr, nc, n_num)
                elif n_num == 1:  # 1인 경우 -1 변경 처리만 해줌
                    arr[nr][nc] = -1
            else:  # 범위를 벗어나면 바로 break
                break


# 어느 벽돌 깰지 선택
def choose_brick(cnt_N, curr_destroy):
    global max_destroy, arr

    # 깬 벽돌 개수가 전체 벽돌 개수와 같은 경우
    if curr_destroy == cnt_bricks:
        max_destroy = curr_destroy
        return

    # N번 다 기회를 쓴 경우
    if cnt_N == N:
        if curr_destroy > max_destroy:
            max_destroy = curr_destroy
        return

    # 왼쪽->오른쪽 방향으로 1또는 그 이상의 숫자 찾음
    for i in range(W):
        for j in range(H):  # 행마다 처음 숫자가 나오는 부분을 찾음
            if arr[i][j] > 1:  # 1 이상인 경우 dfs 돌려서 벽돌깨고 break
                temp_arr = make_arr(arr)  # 재귀에서 빠져나왔을 때 배열을 되돌리기 위한 함수
                dfs(i, j, arr[i][j])
                arr[i][j] = -1  # 시작점 -1로 변경

                # -1로 된 벽돌들 제거 + 제거된 벽돌 개수 세기
                destroy = 0
                for i in range(W):
                    for j in range(H):
                        if arr[i][j] == -1:
                            destroy += 1
                            arr[i].pop(j)  # 해당 인덱스 pop
                            arr[i].insert(0, 0)  # 0번째에 0 insert

                choose_brick(cnt_N + 1, curr_destroy + destroy)  # 현재 깬 벽돌 개수에 새로 깬 벽돌 개수 추가해서 인자로 전달
                arr = temp_arr  # 이전 arr로 되돌려줌
                break
            elif arr[i][j] == 1:  # 1인 경우 바로 처리
                arr[i][j] = 0
                choose_brick(cnt_N + 1, curr_destroy + 1)  # 현재 깬 벽돌 개수에 1 추가해서 인자로 전달
                arr[i][j] = 1  # 되돌리는 함수 굳이 쓸 필요 없기 때문에 바로 처리
                break


T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())  # N: 벽돌깨는 횟수, W: 가로, H: 세로
    bricks = [list(map(int, input().split())) for _ in range(H)]
    max_destroy = 0  # 최대한 깬 벽돌 개수
    cnt_bricks = 0  # 원래 벽돌 개수
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]

    # 배열을 왼쪽으로 90도 회전
    arr = [[] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            arr[j].append(bricks[i][j])
            if bricks[i][j]:
                cnt_bricks += 1  # 전체 벽돌 개수도 같이 세줌
    for i in range(W):
        print(arr[i])
    choose_brick(0, 0)

    print('#{} {}'.format(t, cnt_bricks - max_destroy))
