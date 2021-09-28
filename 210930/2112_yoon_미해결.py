import sys
sys.stdin = open('input_2112.txt')


def check(films):
    for j in range(W):
        line = ''
        for i in range(D):
            line += str(films[i][j])
        if '1'*K not in line and '0'*K not in line:
            return False
    return True

def dfs(cnt, start, films):
    global ans
    if cnt >= ans:
        return
    if check(films):
        if cnt < ans:
            ans = cnt
        return
    else:
        for i in range(start, D):



T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    ans = 99999

    if check(films):
        ans = 0
    else:
