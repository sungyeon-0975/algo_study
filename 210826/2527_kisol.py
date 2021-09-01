import sys

input = sys.stdin.readline

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if (p1 < x2) or (y1 > q2) or (x1 > p2) or (q1 < y2):  # 공통부분 없음
        print('d')
    elif (x1 == p2 and y1 == q2) or (p1 == x2 and q1 == y2) or (x1 == p2 and q1 == y2) or (p1 == x2 and y1 == q2):  # 점
        print('c')
    elif x1 == p2 or y1 == q2 or x2 == p1 or y2 == q1:  # 선
        print('b')
    else:
        print('a')  # 직사각형

# for _ in range(4):
#     x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
#
#     if (p1 < x2) or (y1 > q2) or (x1 > p2) or (q1 < y2):  # 공통부분 없음
#         print('d')
#     elif x1 == p2:
#         if y1 == q2 or q1 == y2:
#             print('c')
#         elif y1 == q2:
#             print('b')
#         else:
#             print('a')
#     elif p1 == x2:
#         if q1 == y2 or y1 == q2:
#             print('c')
#         elif y2 == q1:
#             print('b')
#         else:
#             print('a')
#     else:
#         print('a')  # 직사각형