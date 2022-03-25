def solution(n, computers):
    network = list(range(n))                # 컴퓨터들 서로간 연결 정보

    def union(x, y):                        # 컴퓨터 두대 연결
        network[find(y)] = find(x)          # 각 연결된 컴퓨터의 대표 컴퓨터를 연결
    
    def find(x):                            # 해당 컴퓨터 네트워크의 대표 컴퓨터 검색
        if x != network[x]:                 # 현재 컴퓨터가 대표 컴퓨터가 아니라면
            network[x] = find(network[x])   # 대표 컴퓨터를 찾음
        return network[x]
    
    for i in range(n):                      # 컴퓨터들 연결 정보 반복
        for j in range(i+1, n):
            if computers[i][j]:             # i와 j가 연결되어 있다면
                union(i, j)                 # i와 j 연결 시키기
                
    for i in range(n):                      # 모든 컴퓨터들 네트워크의 대표 컴퓨터로 연결관계 정리
        find(i)
        
    print(network)

    return len(set(network))                # 네트워크 개수 카운트

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))