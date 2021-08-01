import sys

a,b = map(int, sys.stdin.readline().split())

A = set()

num1 = map(int,sys.stdin.readline().split())
A.update(num1)

B = set()

num2 = map(int,sys.stdin.readline().split())
B.update(num2)

set1 = A-B
set2 = B-A

print(len(set1|set2))
