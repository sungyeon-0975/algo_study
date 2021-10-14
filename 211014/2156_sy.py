'''
80ms
'''
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    l = [int(input()) for _ in range(n)]
    v0, v1, v2 = 0, l[0], 0
    for i in range(1, n):
        v0, v1, v2 = max(v0, v1, v2), v0 + l[i], v1 + l[i]
    print(max(v0, v1, v2))

