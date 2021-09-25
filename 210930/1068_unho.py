"""
Memory - 29200 KB
Time - 64 ms
"""


import sys
sys.stdin = open('input_1068.txt')


def dfs(node):                                          # dfs 탐색
    global answer
    stack = [node]
    while stack:
        node = stack.pop()
        if len(linked[node]) == 1:                      # 자식 노드가 없으면 리프 노드 갯수 추가
            answer += 1
            
        for idx in range(1, len(linked[node])):         # 자식 노드 탐색
            stack.append(linked[node][idx])         
        

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
D = int(sys.stdin.readline())

linked = {}                             # 연결 관계 / 0번 인덱스가 부모 노드, 그 이후는 자식 노드들 (이진 트리라는 명시가 없어서 리스트 형태 이용)
start_node = -1                         # 최상위 루트 노드가 0이 아닐수 있으므로
answer = 0                              # 리프 노드 카운트

for idx in range(N):
    if not linked.get(idx):             # 부모 노드 입력
        linked[idx] = [li[idx]]
    else:
        linked[idx][0] = li[idx]

    if li[idx] == -1:                   # 최상위 루트 노드
        start_node = idx
        continue

    if not linked.get(li[idx]):         # 부모노드에서 자식 노드 리스트 추가
        linked[li[idx]] = [-1, idx]
    else:
        linked[li[idx]].append(idx)

try:                                    # 최상위 루트 노드 삭제시 그 부모는 -1 이므로 키에러 발생
    linked[li[D]].remove(D)             # 삭제하는 노드 값 변경
except:                                 # 최상위 루트 노드 삭제시 결과 반환 후 종료
    print(answer)    
else:                                   # 정상적일 경우
    dfs(start_node)                     # dfs 탐색
    print(answer)
