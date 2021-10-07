"""
29200KB 76ms
29200KB 68ms

결국 전부 절반으로 최대한 쪼갠다음에 이어붙이면 된다.
"""

import sys
sys.stdin = open('input_1094.txt')

for test in range(1,1+int(input())):
    X = int(input())
    answer = 0
    for i in range(7):
        if X & (1<<i):
            answer += 1

    print(answer)


    # print(sum(list(map(int,(bin(X)[2:])))))
