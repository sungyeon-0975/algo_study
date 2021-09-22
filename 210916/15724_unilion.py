import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

'''

'''
N, M = map(int, input().split())
NM_list = []
for n in range(N):
    NM_list.append(list(map(int,input().split())))
K = int(input())
K_list = []

for k in range(K):
    result = 0
    x1, y1, x2, y2 = map(int, input().split())

    # for x in range(x1 - 1, x2):
    #     for y in range(y1 - 1, y2):
    #         result += NM_list[x][y]

    # result += sum(sum(NM_list[x1-1:x2][y1-1:y2],[]))
    
    print(result)