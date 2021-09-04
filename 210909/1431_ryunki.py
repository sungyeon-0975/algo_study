import sys
"""
29200KB 88ms
"""

# 길이, 받아올때 숫자면은 모두 더해주고 , 나머지는 정렬해주면 자연스레 된다. 3번의 정렬을 한번에 한다? 바로 튜플로 받아서 람다로간다
sys.stdin = open('input_1431.txt')
T = int(input())
N = int(input())

data = []
for i in range(N):
    NEW = input()
    msum = 0
    for j in NEW:
        if j.isdigit():
            msum += int(j)
    data.append((msum, NEW))
data.sort(key=lambda x: (len(x[1]), x[0], x[1]))
for i in data:
    print(i[1])
