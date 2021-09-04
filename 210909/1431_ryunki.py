import sys
"""
29200KB 88ms
"""
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
