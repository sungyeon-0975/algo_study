import sys
# KB / ms
# input = sys.stdin.readline
'''

'''

sys.stdin = open('input_18222.txt')


T = int(input())

for _ in range(T):
    N = int(input())
    X = [0]
    while len(X) <= N:
        # 2배
        X.extend(X)
        # 반전
        for i in range(len(X) // 2):
            X[i] = 0 if X[i] == 1 else 1

    print(X[N])