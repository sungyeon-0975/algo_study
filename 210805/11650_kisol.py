import sys

input = sys.stdin.readline

T = int(input())
points = []

for i in range(T):
    points.append(tuple(map(int, input().split())))

for point in sorted(points):
    print(*point)

# sorted_points = sorted(points, key=lambda x: [x[0], x[1]])

# for i in range(len(points) - 1):
#     for j in range(i + 1, len(points)):
#         if points[i][0] > points[j][0]:
#             points[i], points[j] = points[j], points[i]
#         elif points[i][0] == points[j][0] and points[i][1] > points[j][1]:
#             points[i], points[j] = points[j], points[i]