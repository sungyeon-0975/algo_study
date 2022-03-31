def solution(triangle):
    answer = 0
    l = len(triangle)
    
    for i in range(1,l):
        for j in range(i+1):
            tmp = []
            for dr, dc in [(-1,-1),(-1,0)]:
                if i == 0:
                    continue
                if j + dc < 0 or j + dc == i:
                    continue
                tmp.append(triangle[i+dr][j+dc])
            triangle[i][j] += max(tmp)

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
