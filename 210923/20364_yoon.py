import sys
# input = sys.stdin.readline
sys.stdin = open('input_20364.txt')


'''
46612KB / 952ms
'''


N, Q = map(int, input().split())
visited = set() # list로 했을 때 시간초과

for _ in range(Q):
    duck = int(input())
    temp = duck
    res = 0

    # 이 과정 재귀함수로 해도 시간초과
    while temp > 1:
        if temp in visited:
            res = temp
        temp //= 2
    visited.add(duck)

    print(res)