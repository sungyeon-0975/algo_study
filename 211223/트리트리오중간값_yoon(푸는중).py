def solution(n, edges):
    answer = 0
    tree = [[] for _ in range(n+1)]
    for i in range(len(edges)):
        v1, v2 = edges[i]
        tree[v1].append(v2)
        tree[v2].append(v1)
    print(tree)

    return answer

print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(5, [[1,5],[2,5],[3,5],[4,5]]))