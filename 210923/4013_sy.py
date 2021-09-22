import sys
sys.stdin = open('input/4013_input.txt')

def rotate(num, d, num_d):
    global i_list
    if 3 > num > 0 and magnet[num+num_d][(i_list[num+num_d] - 2*num_d + 8) % 8] != magnet[num][(i_list[num] + 2*num_d + 8) % 8]:
        rotate(num + num_d, -1*d, num_d)
    i_list[num] = (i_list[num] - d + 8) % 8

t = int(input())
for t_idx in range(1, t+1):
    k = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    i_list = [0]*4
    for _ in range(k):
        num, d = map(int, input().split())
        num -= 1

        if num > 0 and magnet[num-1][(i_list[num-1] + 2) % 8] != magnet[num][(i_list[num] + 6) % 8]:
            rotate(num - 1, -1*d, -1)
        if num < 3 and magnet[num+1][(i_list[num+1] + 6) % 8] != magnet[num][(i_list[num] + 2) % 8]:
            rotate(num + 1, -1*d, 1)
        i_list[num] = (i_list[num] - d + 8) % 8

    res = sum(map(lambda x: (2**x[0])*magnet[x[0]][x[1]], enumerate(i_list)))
    print('#{} {}'.format(t_idx, res))

