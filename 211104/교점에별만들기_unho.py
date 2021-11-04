def comb(arr, idx, n, r, k):
    global selected, coor, min_x, min_y, max_x, max_y

    if idx >= n or r <= 0:
        if selected[0] and selected[1]:
            a = selected[0][0]
            b = selected[0][1]
            e = selected[0][2]
            
            c = selected[1][0]
            d = selected[1][1]
            f = selected[1][2]

            if (a*d - b*c) != 0:
                x = (b*f - e*d) / (a*d - b*c)
                y = (e*c - a*f) / (a*d - b*c)

                if float(x).is_integer() and float(y).is_integer():
                    x, y = int(x), int(y)

                    if min_x >= x: min_x = x
                    if min_y >= y: min_y = y
                    if max_x <= x: max_x = x
                    if max_y <= y: max_y = y

                    coor.add((y, x))
        return
    
    selected[k] = arr[idx]
    comb(arr, idx+1, n, r-1, k-1)
    selected[k] = []
    comb(arr, idx+1, n, r, k)  


def solution(line):
    global selected, coor, min_x, min_y, max_x, max_y

    selected = [[], []]
    coor = set()
    min_x, min_y, max_x, max_y = 1e20, 1e20, -1e20, -1e20
    answer = []
    
    comb(line, 0, len(line), 2, 0)
    
    for i in range(max_y, min_y-1, -1):
        tmp = ''
        for j in range(min_x, max_x+1):
            if (i, j) in coor:
                tmp += '*'
            else:
                tmp += '.'
        answer.append(tmp)
        
    return answer


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))