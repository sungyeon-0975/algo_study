import sys
input = sys.stdin.readline

input()
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a.union(b)) - len(a.intersection(b)))