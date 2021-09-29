import sys
input = sys.stdin.readline

tc = int(input())

for t in range(tc):
    result = 0
    K = int(input()) # 자석 회전시킨 횟수

    mag = []
    for _ in range(4):
        mag.append(list(map(int, input().split())))

    K_list = []
    for _ in range(K):
        K_list.append(list(map(int, input().split())))

    

    print("#{} {}".format(t, result))