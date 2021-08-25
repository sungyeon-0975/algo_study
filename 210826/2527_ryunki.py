import sys

sys.stdin = open("input.txt")
# 이게맞아.........
for _ in range(4):
    data = list(map(int, input().split()))

    answer = 'a'

    if data[3] < data[5] or data[7] < data[1] or data[0] > data[6] or data[2] < data[4]:
        answer = 'd'

    if data[2] == data[4]:
        if data[3] == data[5] or data[1] == data[7]:
            answer = 'c'
        else:
            answer = 'b'

    if data[0] == data[6]:
        if data[1] == data[7] or data[3] == data[5]:
            answer = 'c'
        else:
            answer = 'b'

    if data[3] == data[5]:
        if data[2] == data[4] or data[6] == data[0]:
            answer = 'c'
        else:
            answer = 'b'

    if data[7] == data[1]:
        if data[2] == data[4] or data[6] == data[0]:
            answer = 'c'
        else:
            answer = 'b'

    print(answer)
