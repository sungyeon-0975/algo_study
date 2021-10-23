def dfs(visited, N_list, n):    # visited랑 N_list가 없으니 not defined 떠서 넣어줌
    cnt = 0         # cnt 0으로 초기화
    stack = [1]     # stack에 1을 넣어줌
    while stack:    # stack이 없을 때 까지 진행
        y = stack.pop()     # y에 stack 마지막 값을 넣어줌
        visited[y] = 1      # y 방문 표시
        cnt += 1            # cnt + 1
        for x in range(2, n + 1):   # 2부터 n + 1까지 순회 (1은 어차피 자기 자신, 연결 x)
            if N_list[y][x] == 1:   # y와 연결된 곳이 있으면
                if not visited[x]:  # x 가 방문 표시가 안 되어 있으면
                    stack.append(x) # stack에 x를 넣어줌
    return cnt  # cnt 값 return

n = 9   # 예시 1테스트
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]    # 예시 1 테스트
N_list = [[0] * (n + 1) for _ in range(n + 1)]  # 인접 행렬
visited = [0] * (n + 1) # 방문 표시
result = n      # 결과값, 최대 값은 n - 1
for i in wires: # 연결 정보를 하나씩 순회
    N_list[i[0]][i[1]] = 1  # 인접 행렬에 서로 연결
    N_list[i[1]][i[0]] = 1

for j in wires: # 연결 정보 하나씩 순회
    N_list[j[0]][j[1]] = 0  # 연결을 끊음
    N_list[j[1]][j[0]] = 0

    temp1 = dfs(visited, N_list, n) # dfs 함수 돌려서 나온 count 수 담음
    temp2 = n - temp1   # 나머지는 자연스럽게 n - temp1개
    temp3 = abs(temp1 - temp2)  # temp3에 두 개의 차이 값을 담음
    if result > temp3:  # 만약 result보다 temp3가 작으면
        result = temp3  # result 갱신

    visited = [0] * (n + 1) # 방문 표시 초기화
    N_list[j[0]][j[1]] = 1  # 다시 연결
    N_list[j[1]][j[0]] = 1

print(result)
