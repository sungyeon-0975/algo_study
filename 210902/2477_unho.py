import sys
sys.stdin = open('input_2477.txt')

K = int(input())
num_list = [list(map(int, input().split())) for _ in range(6)]

max_width = max(filter(lambda x: x[0]==1 or x[0]==2, num_list), key=lambda x: x[1])
max_height = max(filter(lambda x: x[0]==3 or x[0]==4, num_list), key=lambda x: x[1])

max_width_idx = num_list.index(max_width)
max_height_idx = num_list.index(max_height)

if (max_width_idx + 1) % 6 == max_height_idx:
    minus_width_idx = (max_width_idx + 4) % 6
    minus_height_idx = (max_width_idx + 3) % 6
else:
    minus_width_idx = (max_width_idx + 2) % 6
    minus_height_idx = (max_width_idx + 3) % 6

answer = (max_width[1] * max_height[1]) - (num_list[minus_width_idx][1] * num_list[minus_height_idx][1])
print(answer * K)