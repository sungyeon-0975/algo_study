n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0


def clean_bot(r, c, d):
    global cnt
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    for i in range(1, 5):
        nr, nc = direction[(d - i) % 4]
        nr += r
        nc += c

        if room[nr][nc] == 0:
            clean_bot(nr, nc, (d - i) % 4)
            return None

    nr, nc = direction[(d + 2) % 4]
    nr += r
    nc += c

    if room[nr][nc] == 1:
        return None
    else:
        clean_bot(nr, nc, d)


clean_bot(r, c, d)
print(cnt)
