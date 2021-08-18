import sys
input = sys.stdin.readline

width, height = map(int, input().split())
width_points = [0, width]
height_points = [0, height]
max_area = 0

T = int(input())

for _ in range(T):
    dir, point = map(int, input().split())
    if dir: #세로방향
        width_points.append(point)
    else: #가로방향
        height_points.append(point)

width_points.sort()
height_points.sort()

for i in range(len(width_points) - 1):
    for j in range(len(height_points) - 1):
        area = (width_points[i + 1] - width_points[i]) * (height_points[j + 1] - height_points[j])
        if area > max_area:
            max_area = area

print(max_area)