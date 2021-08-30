import sys

sys.stdin = open('input_2559.txt')

input = sys.stdin.readline

for test in range(1, 3):
    N, K = map(int, input().split())

    data = list(map(int, input().split()))

    i = K
    temp = sum(data[:K])
    answer = temp

    while i < N:
        temp += data[i]
        temp -= data[i - K]
        if temp > answer:
            answer = temp
        i += 1
    if N != K:
        print(answer)
    else:
        print(temp)


    # answer = 0
    # for i in range(len(data)-K+1):
    #     msum = 0
    #     for j in range(K):
    #         msum+= data[i+j]
    #     answer = max(answer,msum)
    #
    # print(answer)
