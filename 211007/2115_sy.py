
def max_profit(row):
    profits = []
    for i in range(n-m+1):
        profits.append(get_max_squared_sum(sorted(honeycomb[row][i:i + m], reverse=True)))
    return max(profits)

def get_max_squared_sum(sorted_l):
    max_squared_sum = 0
    for i in range(m):
        acc = 0
        squared_sum = 0
        for j in range(i, m):
            if acc +  sorted_l[j] <=  c:
                acc += sorted_l[j]
                squared_sum += sorted_l[j]**2
        if max_squared_sum > squared_sum:
            return max_squared_sum
        max_squared_sum = squared_sum
    return max_squared_sum

if __name__ == "__main__":
    t = int(input())
    for idx in range(1, t+1):
        n, m, c = map(int, input().split())
        honeycomb = [list(map(int, input().split())) for _ in range(n)]
        res = sum(sorted([max_profit(i) for i in range(n)], reverse=True)[:2])
        print('#{} {}'.format(idx, res))


