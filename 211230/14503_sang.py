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


# from collections import deque


# # 왼쪽으로 돌면서 청소가능할 경우 dq에 추가후 True 리턴
# def cleanalble():
#     for i in range(1, 5):
#         nr, nc = direction[(d - i) % 4]
#         nr += r
#         nc += c

#         if room[nr][nc] == 0:
#             dq.append([nr, nc, (d - i) % 4])
#             return True

#     return False


# n, m = map(int, input().split())
# r, c, d = map(int, input().split())
# room = [list(map(int, input().split())) for _ in range(n)]
# direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# dq = deque([[r, c, d]])
# cnt = 0

# while dq:
#     r, c, d = dq.popleft()

#     if room[r][c] == 0:
#         room[r][c] = 2
#         cnt += 1

#     # 왼쪽으로 돌면서 청소가능 확인 후 dq에 추가
#     if cleanalble():
#         continue

#     #   청소 불가능 할 경우
#     nr, nc = direction[(d + 2) % 4]
#     nr += r
#     nc += c
#     #   후진이 불가능할 경우 종료
#     if room[nr][nc] == 1:
#         break
#     #   후진이 가능할 경우 dq 추가
#     else:
#         dq.append([nr, nc, d])

# print(cnt)
