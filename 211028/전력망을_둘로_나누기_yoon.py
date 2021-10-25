def make_set(x):
    global p
    p[x] = x

def find_set(x):
    global p
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    global p
    p[find_set(y)] = find_set(x)

def solution(n, wires):
    global p
    answer = n
    p = [0] * (n+1)
    for i in range(len(wires)):
        p = [0] * (n+1)
        for j in range(n+1):
            make_set(j)

        temp = wires[::]
        temp.remove(wires[i])

        for k in range(len(temp)):
            x, y = temp[k]
            if find_set(x) != find_set(y):
                union(x, y)

        g1, g2 = 1, 0
        for l in range(2, n+1):
            if find_set(l) == find_set(1):
                g1 += 1
            else:
                g2 += 1

        if abs(g1-g2) < answer:
            answer = abs(g1-g2)

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))