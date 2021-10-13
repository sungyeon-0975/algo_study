import sys

sys.stdin = open('input.txt')
from pandas import DataFrame

"""
66228kb, 457ms
1. 위칸들 중에서 숫자 있는거로 n번은 깨야됨 무조건 재귀로 풀어야 하나 구슬 수가 더많거나 구슬을 다 쓰는 경우가 있을 수 있음
2. 탐색중에 1보다 큰값을 만나면 좌표값이랑 제거해야하는 칸수를 저장 find start position
3. remove block 
4. rematch
5. 탐색 반복 (N만큼)
"""
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def destroy(n, data):  # ballnumber, breakable_brick_num, data_for_now
    global answer

    total = 0  # can destroy block number
    for i in data:
        for j in i:
            if j:
                total += 1

    if n == N or not total:  # 구슬이 더많거나 # 구슬을 다쓴 경우
        answer = min(answer, total)
        return

    # find position
    for j in range(W):
        stack = []
        for i in range(H):
            if data[i][j]:  # must search
                copy_data = [x[:] for x in data]  # don't change data
                stack = [(i, j, data[i][j])]  # add
                copy_data[i][j] = 0  # start
                break
        if not stack:
            continue

        # remove
        while stack:
            x, y, length = stack.pop()
            for c in range(1, length):  # ~length-1 아니면 한방향 결정나면 그만큼 움직이게 설정?
                for dx, dy in move:
                    nx = x + dx * c  # 아 이거 한칸씩만움직이네
                    ny = y + dy * c
                    if 0 <= nx < H and 0 <= ny < W and copy_data[nx][ny]:
                        if copy_data[nx][ny] > 1:
                            stack.append((nx, ny, copy_data[nx][ny]))
                        copy_data[nx][ny] = 0

        # rematch
        for h in range(W):
            temp = H - 1
            for k in range(H - 1, -1, -1):
                if copy_data[k][h]:
                    copy_data[temp][h], copy_data[k][h] = copy_data[k][h], copy_data[temp][h]
                    temp -= 1

        destroy(n + 1, copy_data)


for test in range(1, 1 + int(input())):
    N, W, H = map(int, input().split())
    mydata = list(list(map(int, input().split())) for _ in range(H))
    answer = 1e9

    destroy(0, mydata)

    print('#{} {}'.format(test, answer))