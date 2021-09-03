import sys
sys.stdin = open('input_1431.txt')

'''
둘 다 29200KB / 84ms
'''

# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     numbers = []
#     for _ in range(N):
#         serial = input()
#         num_sum = 0
#         for i in range(len(serial)):
#             if serial[i].isdigit():
#                 num_sum += int(serial[i])
#         numbers.append((serial, len(serial), num_sum))
#     numbers.sort(key=lambda x:(x[1], x[2], x[0]))
#     for n in range(N):
#         print(numbers[n][0])

def num_sum(serial): # 숫자 합 계산
    ns = 0
    for i in range(len(serial)):
        if serial[i].isdigit():
            ns += int(serial[i])
    return ns

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    numbers = []

    for _ in range(N):
        serial = input()
        numbers.append(serial)

    numbers.sort(key = lambda x:(len(x), num_sum(x), x)) # key tuple 안에 넣어주는 순서대로 정렬됨

    for n in range(N):
        print(numbers[n])