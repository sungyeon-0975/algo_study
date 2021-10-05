import sys

# 29200KB / 76ms
# input = sys.stdin.readline
'''
처음에는 64cm 막대 하나만 가지고 있다. 이때, 합이 X보다 크다면, 아래와 같은 과정을 반복한다.
1. 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
2. 만약, 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다.
이제, 남아있는 모든 막대를 풀로 붙여서 Xcm를 만든다. 
몇 개의 막대를 풀로 붙여서 Xcm를 만들 수 있는지 출력
Check Point) 절반으로 나누고 이런거는 비트마스킹으로도 생각해보자
'''
sys.stdin = open('input_1094.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(7):  # 1~64
        if N & (1 << i):  # 해당 이진법 자리수가 1이면 막대기 한개 쓴 것
            cnt += 1
    print(cnt)
