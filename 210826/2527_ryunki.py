import sys

sys.stdin = open("input.txt")
# 이게맞아.........??
# if 따로 하나하나보는거고 elif는 한뭉테기로 보는거고
for _ in range(4):
    data = list(map(int, input().split()))

    answer = 'a'

    if data[3] < data[5] or data[7] < data[1] or data[0] > data[6] or data[2] < data[4]:
        answer = 'd'

    elif data[2] == data[4]:
        if data[3] == data[5] or data[1] == data[7]:
            answer = 'c'
        else:
            answer = 'b'

    elif data[0] == data[6]:
        if data[1] == data[7] or data[3] == data[5]:
            answer = 'c'
        else:
            answer = 'b'

    elif data[3] == data[5]:
        if data[2] == data[4] or data[6] == data[0]:
            answer = 'c'
        else:
            answer = 'b'

    elif data[7] == data[1]:
        if data[2] == data[4] or data[6] == data[0]:
            answer = 'c'
        else:
            answer = 'b'

    print(answer)


# def square(n):
#     x1, y1, x2, y2, x3, y3, x4, y4 = n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7]
#     if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
#         return 'd'
#     elif (x2 == x3 and y2 == y3) or (x3 == x2 and y1 == y4) or (x4 == x1 and y3 == y2) or (x4 == x1 and y4 == y1):
#         return 'c'
#     elif ((x3 == x2 or x4 == x1) and y3 < y2 and y4 > y1) or ((y2 == y3 or y4 == y1) and x4 > x1 and x3 < x2):
#         return 'b'
#     else:
#         return 'a'
#
# for _ in range(4):
#     s_list = list(map(int, input().split()))
#     print(square(s_list))