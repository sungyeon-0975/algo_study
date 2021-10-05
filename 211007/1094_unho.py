"""
Memory - 29200 KB (28.51 MB)
Time - 116 ms
"""


import sys

X = int(sys.stdin.readline())

answer = 0
for i in range(7):
    if X & (1 << i):
        answer += 1

print(answer)