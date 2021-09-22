'''
실행시간 : 188ms
'''
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        for _ in range(m):
            a,b = map(int, input().split())
        print(n-1)