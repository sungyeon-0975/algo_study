import sys
sys.stdin = open('input.txt')

def dfs(month, cost):
    global res
    if month >= 12:
        if res > cost:
            res = cost
    else:
        for i in range(2):
            dfs(*func[i](month, cost))
        if month <= 9:
            dfs(*func[2](month, cost))


t = int(input())
func = [lambda x, y: (x+1, prices[0]*monthly_plan[x] + y),
        lambda x, y: (x+1, prices[1] + y),
        lambda x, y: (x+3, prices[2] + y)]
for idx in range(1, t+1):
    prices = list(map(int, input().split()))
    monthly_plan = list(map(int, input().split()))

    res = prices[3]
    dfs(0, 0)

    print('#{} {}'.format(idx, res))