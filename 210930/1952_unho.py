import sys
sys.stdin = open('input.txt')


def dfs(node, ans):                         # dfs 탐색
    global answer

    if node >= 12:
        if answer > ans:
            answer = ans
        return
    elif ans > answer:                      # 이미 비싸지면 해당 경우 종료
        return
    
    dfs(node+1, ans + (day * plan[node]))   # 1일권
    dfs(node+1, ans + month)                # 1달권
    dfs(node+3, ans + three_month)          # 3달권


T = int(input())

for tc in range(1, T+1):
    day, month, three_month, year = map(int, input().split())
    plan = list(map(int, input().split()))
    answer = year

    dfs(0, 0)

    print('#{} {}'.format(tc, answer))