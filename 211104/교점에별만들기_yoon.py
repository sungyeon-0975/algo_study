# test 27, 28 (시간초과) 빼고 통과

def solution(line):
    points = []
    max_x, min_x, max_y, min_y = -987654321, 987654321, -987654321, 987654321
    # 모든 가능성에 대해 교점 좌표 구하기
    # 그 중에서 정수인 애들만 따로 받아줌
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i, len(line)):
            c, d, f = line[j]
            if a*d - b*c:
                x = (b*f - e*d)/(a*d - b*c)
                y = (e*c - a*f)/(a*d - b*c)
                if x.is_integer() and y.is_integer() and (int(x), int(y)) not in points:
                    x, y = int(x), int(y)
                    max_x, min_x, max_y, min_y = max(max_x, x), min(min_x, x), max(max_y, y), min(min_y, y)
                    points.append((x, y))
    result = [['.' for _ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]
    for x, y in points:
        result[max_y-y][x-min_x] = '*'
    return [''.join(r) for r in result]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))