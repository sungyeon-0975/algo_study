import sys
sys.stdin = open('input_15683.txt')

for test in range(1,1+int(input())):
    N,M = map(int,input().split())
    data=[list(input().split()) for _ in range(N)]

    print(data)


    0 0 0 0 0 #
    0 2 # # 0 #
    0 # 0 0 6 #
    0 6 # # 2 #
    0 # 0 0 # #
    # # # # # 5