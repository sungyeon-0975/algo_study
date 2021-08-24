if __name__ == "__main__":
    n = int(input())
    tower = [list(map(int, input().split())) for _ in range(n)]
    oppo_idx = [5,3,4,1,2,0]
    res = 0
    for bottom_val in range(1,7):
        total = 0
        for floor in range(n):
            bottom_idx = tower[floor].index(bottom_val)
            except_idx = {bottom_idx, oppo_idx[bottom_idx]}
            max_val = 0
            for j in range(6):
                if j not in except_idx:
                    max_val = max(max_val, tower[floor][j])
            total += max_val
            bottom_val = tower[floor][oppo_idx[bottom_idx]]
        res = max(total, res)
    print(res)

