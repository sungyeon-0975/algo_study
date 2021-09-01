import sys
# input = sys.stdin.readline
sys.stdin = open('input_2477.txt')

'''
s1 : 84ms / s2 : 80ms
'''

# K = int(input())
# dir = [0] * 5 # 0, 동:1, 서:2, 남:3, 북:4 길이
# d = [0] * 6 # 입력받는 방향
# l = [0] * 6 # 입력받는 길이
#
# for i in range(6):
#     d[i], l[i] = map(int, input().split())
#
# # 방향을 돌면서 dir에 최종적으로 쓸 바깥 길이와, 안쪽 박스 길이 구하기
# for i in range(6):
#     if d.count(d[i]) == 1: # 방향이 한번밖에 안 나온 경우 바깥 길이
#         dir[d[i]] = l[i]
#     elif d[i] == d[(i + 2) % 6]: # 중간 기준으로 앞뒤로 같은 방향이 나온 경우 안쪽 박스 길이
#         dir[d[(i + 1) % 6]] = l[(i + 1) % 6]
#
# large_w, large_h = max(dir[1], dir[2]), max(dir[3], dir[4]) # 둘중
# small_w, small_h = min(dir[1], dir[2]), min(dir[3], dir[4])
#
# print((large_w * large_h - small_w * small_h) * K)


K = int(input())

d = [0] * 6 # 입력받는 방향
l = [0] * 6 # 입력받는 길이
large_box = 1
small_box = 1

for i in range(6):
    d[i], l[i] = map(int, input().split())

# 방향을 돌면서 dir에 최종적으로 쓸 바깥 길이와, 안쪽 박스 길이 구하기
for i in range(6):
    if d.count(d[i]) == 1: # 방향이 한번밖에 안 나온 경우 바깥 길이
        large_box *= l[i]
    elif d[i] == d[(i + 2) % 6]: # 중간 기준으로 앞뒤로 같은 방향이 나온 경우 안쪽 박스 길이
        small_box *= l[(i + 1) % 6]

print((large_box - small_box) * K)