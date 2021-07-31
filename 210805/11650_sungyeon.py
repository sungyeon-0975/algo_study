import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    l = [tuple(map(int,input().split())) for _ in range(n)]
    l.sort(key = lambda x: (x[0],x[1]))
    for a,b in l:
        print(a,b)