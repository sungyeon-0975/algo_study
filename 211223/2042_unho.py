import sys
from math import ceil, log2
sys.stdin = open('input.txt')


# 초기 세그먼트 트리 생성
def initial(node, left, right):                                 # 트리의 현재 노드 / 현재 노드의 숫자 범위 시작 / 현재 노드의 숫자 범위의 끝
    if left >= right:                                           # 리프 노드에 도착하면
        segment_tree[node] = num[left]                          # 리프 노드에 숫자 저장
        node_link[left] = node                                  # 리프 노드의 인덱스 저장
        return segment_tree[node]                               # 리프 노드의 값 반환
    
    left_sum = initial(node*2, left, (left+right)//2)           # 왼쪽 구역의 합 (재귀로 트리의 밑으로 내려감)
    right_sum = initial(node*2+1, (left+right)//2+1,right)      # 오른쪽 구역의 합
    segment_tree[node] = left_sum + right_sum                   # 현재 노드의 값 = 왼쪽 구역의 누적합 + 오른쪽 구역의 누적합

    return segment_tree[node]                                   # 현재 노드의 부모를 위해 현재 노드의 값 반환


# 특정 구간의 합 반환
def section_sum(node, left, right):                                 # 트리 현재 노드 / 노드의 범위 시작 / 노드의 범위 끝
    if left > target_right or right < target_left:                  # 현재 노드가 찾으려는 범위의 누적합이 아니면 0 반환
        return 0
    elif target_left <= left and right <= target_right:             # 현재 노드가 찾으려는 범위에 완전히 속하면 현재 노드의 값 반환
        return segment_tree[node]
    
    left_sum = section_sum(node*2, left, (left+right)//2)           # 왼쪽 자식 노드 탐색
    right_sum = section_sum(node*2+1, (left+right)//2 + 1, right)   # 오른쪽 자식 노드 탐색
    return left_sum + right_sum                                     # 구해진 합 반환


# 특정 노드의 값 변경에 따른 세그먼트 트리 갱신
def update(node):                                                           # 현재 노드의 변호
    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]      # 현재 노드의 값은 왼쪽 자식과 오른쪽 자식의 합

    if node != 1:                                                           # 최상위 루트가 아니면, 계속해서 부모 노드를 방문하여 값 변경
        update(node//2)


N, M, K = map(int, sys.stdin.readline().split())            # 수의 개수 / 변경 횟수 / 구간합 구하는 횟수
num = [0] + [int(sys.stdin.readline()) for _ in range(N)]   # 입력받은 숫자 리스트 (편의를 위한 0번 인덱스 추가)
segment_tree = [0] * 2**ceil(log2(N)) * 2                   # 트리의 크기 지정 (log2 를 이용해 (트리의 레벨-1)을 구한다)
node_link = [-1] * (N+1)                                    # 각 숫자가 트리에서 몇번 인덱스에 값이 배정 되었는지 저장하는 변수

initial(1, 0, N-1)                                          # 트리에 값 저장

for _ in range(M+K):                                        
    a, b, c = map(int, sys.stdin.readline().split())        # 연산의 종류 / 시작 인덱스 / 끝 인덱스(변경할 값)

    if a == 1:                                              # 숫자 변경
        leaf_node = node_link[b]                            # 변경할 숫자의 트리 인덱스 구함
        segment_tree[leaf_node] = c                         # 해당 숫자 값 변경
        update(leaf_node//2)                                # 부모 노드들의 값 변경

    elif a == 2:                                            # 구간합 구하기
        target_left = b                                     # 구하려는 범위의 시작
        target_right = c                                    # 구하려는 범위의 끝
        print(section_sum(1, 0, N-1))                       # 구간합 구하기