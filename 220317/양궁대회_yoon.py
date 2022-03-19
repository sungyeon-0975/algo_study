from copy import deepcopy

def solution(n, info):
    max_diff = 0
    max_ryan = []

    def dfs(apeach, ryan, cnt, idx, ryan_list):
        nonlocal max_diff, max_ryan
        if cnt > n:
            return
        if idx == 11:
            diff = ryan - apeach
            if diff > max_diff:
                ryan_list[10] = n - cnt
                max_ryan = ryan_list
                max_diff = diff
            return
        if cnt < n:
            ryan_temp = deepcopy(ryan_list)
            ryan_temp[10-idx] = info[10-idx] + 1    # 무조건 apeach+1 (ryan 점수추가)
            dfs(apeach, ryan+idx, cnt + ryan_temp[10-idx], idx+1, ryan_temp)
        ryan_temp = deepcopy(ryan_list)
        if info[10-idx] > 0:
            dfs(apeach+idx, ryan, cnt, idx+1, ryan_temp)
        else:
            dfs(apeach, ryan, cnt, idx+1, ryan_temp)

    dfs(0, 0, 0, 0, [0]*11)
    return max_ryan if max_ryan else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))