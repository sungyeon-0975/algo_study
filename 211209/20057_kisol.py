import sys

# 43044KB / 2420ms Python3
# 237652KB / 568ms PyPy3
# input = sys.stdin.readline
'''
a값은 소수점 버린거 빼고 나머지값이 할당돼야 함 ㅠㅠ (0.55 아님)
'''

sys.stdin = open('input_20057.txt')


def Tornado():
    global r, c, d, l, ans

    while True:  # (0, 0)에 도착할 때까지
        for _ in range(2):  # 같은 길이로 두 번씩
            d_effects = effects[d]
            for _ in range(l):  # 길이 횟수만큼 실행
                r, c = r + dr[d], c + dc[d]
                sand = arr[r][c]  # 전체 모래 양
                remain = arr[r][c]  # a에 할당할 남은 모래양

                if sand:
                    for i in range(1, 10):  # a영역 제외 비율만큼 모래 날리는 공간
                        nr, nc = r + d_effects[i][0], c + d_effects[i][1]  # 해당 좌표에 행, 열 값 더하기
                        added_sand = int(sand * d_effects[i][2])  # 전체 모래 양에 비율만큼 곱하고 소수점 버리기
                        if 0 <= nr < N and 0 <= nc < N:  # 범위 안이라면
                            arr[nr][nc] += added_sand  # 그 좌표에 해당 모래 양 더하기
                        else:
                            ans += added_sand  # 밖으로 나간 양에 더하기
                        remain -= added_sand  # a에 할당할 남은 모래양에서 빼주기

                    nr, nc = r + d_effects[0][0], c + d_effects[0][1]  # a영역
                    if 0 <= nr < N and 0 <= nc < N:
                        arr[nr][nc] += remain  # a에 할당할 남은 모래양 더하기
                    else:
                        ans += remain

                    arr[r][c] = 0  # y의 모래는 0으로
            if (r, c) == (0, -1):
                return
            d = (d + 1) % 4
        l += 1


T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]  # 좌하우상
    r, c, d, l = N // 2, N // 2, 0, 1  # 행, 열, 방향, 길이
    org_sand = sum(sum(arr, []))
    ans = 0
    # 방향별 [행 방향 이동, 열 방향 이동, 비율]
    effects = [[
        [dr[x], dc[x], 0],
        [2 * dr[x], 2 * dc[x], 0.05],
        [dr[(x + 1) % 4], dc[(x + 1) % 4], 0.07],
        [2 * dr[(x + 1) % 4], 2 * dc[(x + 1) % 4], 0.02],
        [dr[(x + 1) % 4] + dr[x], dc[(x + 1) % 4] + dc[x], 0.1],
        [dr[(x + 1) % 4] + dr[(x + 2) % 4], dc[(x + 1) % 4] + dc[(x + 2) % 4], 0.01],
        [dr[(x + 3) % 4], dc[(x + 3) % 4], 0.07],
        [2 * dr[(x + 3) % 4], 2 * dc[(x + 3) % 4], 0.02],
        [dr[(x + 3) % 4] + dr[x], dc[(x + 3) % 4] + dc[x], 0.1],
        [dr[(x + 3) % 4] + dr[(x + 2) % 4], dc[(x + 3) % 4] + dc[(x + 2) % 4], 0.01],
    ] for x in range(4)]

    Tornado()
    print(ans)
