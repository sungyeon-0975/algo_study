import sys
sys.stdin = open('1963_input.txt')
# input = sys.stdin.readline


def dfs(a, b, cnt):
    global visited, ans
    for i in range(4):
        if not visited[]:

            visited[i]
            dfs()


digit = [1000, 100, 10, 1]
prime = [True] * 10000
for i in range(2, 101):
    for j in range(2, 10000//i):
        if i*j > 10000: break
        prime[i*j] = False

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    ans = 10e9
    visited = [0] * 10000
    dfs(A, B, 0)