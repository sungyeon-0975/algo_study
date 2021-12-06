#	39256KB	1548ms

import sys
input = sys.stdin.readline

def nogada(d, now, r, c):
    global result
    temp = now
    move_left =[(-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02), (-1, 1, 0.01), (1, 1, 0.01),
                (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05)]
    move_right=[(-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02), (-1, -1, 0.01), (1, -1, 0.01),
                (-1, 1, 0.1), (1, 1, 0.1), (0, 2, 0.05)]
    move_up = [(-1, -1, 0.1), (-1, 1, 0.1), (0, 1, 0.07), (0, -1, 0.07), (1, -1, 0.01), (1, 1, 0.01),
               (-2, 0, 0.05), (0, -2, 0.02), (0, 2, 0.02)]
    move_down = [(-1, -1, 0.01), (-1, 1, 0.01), (0, -1, 0.07), (0, 1, 0.07), (0, -2, 0.02), (0, 2, 0.02),
                 (1, -1, 0.1), (1, 1, 0.1), (2, 0, 0.05)]
    move_list = [move_up, move_down, move_right, move_left]
    last_move = [(-1, 0, 1), (1, 0, 1), (0, 1, 1), (0, -1, 1)]

    for i in move_list[d]:
        temp_r = r + i[0]
        temp_c = c + i[1]
        temp_sand = int(temp * i[2])
        now -= temp_sand
        if temp_r < 0 or temp_r >= N or temp_c < 0 or temp_c >= N:
            result += temp_sand
            continue
        N_list[temp_r][temp_c] += temp_sand

    last_r = r + last_move[d][0]
    last_c = c + last_move[d][1]
    if last_r < 0 or last_r >= N or last_c < 0 or last_c >= N:
        result += now
    else:
        N_list[last_r][last_c] += now

N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
middle = [N//2, N//2]
direction = [(-1, 0), (1,0), (0, 1), (0, -1)]
result = 0
for i in range(N - 1):
    if i % 2 == 0:
        for _ in range(i + 1): # left
            middle[0] = middle[0] + direction[3][0]
            middle[1] = middle[1] + direction[3][1]
            temp = N_list[middle[0]][middle[1]]
            N_list[middle[0]][middle[1]] = 0
            nogada(3, temp, middle[0], middle[1])

        for _ in range(i + 1): # down
            middle[0] = middle[0] + direction[1][0]
            middle[1] = middle[1] + direction[1][1]
            temp = N_list[middle[0]][middle[1]]
            N_list[middle[0]][middle[1]] = 0
            nogada(1, temp, middle[0], middle[1])

    else:
        for _ in range(i + 1):  # right
            middle[0] = middle[0] + direction[2][0]
            middle[1] = middle[1] + direction[2][1]
            temp = N_list[middle[0]][middle[1]]
            N_list[middle[0]][middle[1]] = 0
            nogada(2, temp, middle[0], middle[1])

        for _ in range(i + 1):  # up
            middle[0] = middle[0] + direction[0][0]
            middle[1] = middle[1] + direction[0][1]
            temp = N_list[middle[0]][middle[1]]
            N_list[middle[0]][middle[1]] = 0
            nogada(0, temp, middle[0], middle[1])


for _ in range(N):
    middle[0] = middle[0] + direction[3][0]
    middle[1] = middle[1] + direction[3][1]
    temp = N_list[middle[0]][middle[1]]
    N_list[middle[0]][middle[1]] = 0
    nogada(3, temp, middle[0], middle[1])

print(result)