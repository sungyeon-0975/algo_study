import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    l = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n + 1):
        for j in range(1, n+1):
            l[i][j] += l[i-1][j]

    for i in range(1, n+1):
        for j in range(1, n+1):
            l[i][j] += l[i][j-1]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(l[x2][y2] - l[x2][y1-1] - l[x1-1][y2] + l[x1-1][y1-1])



