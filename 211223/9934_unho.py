""" 
Python
    Memory - 29 MB
    Time - 0.068 s
"""
import sys
sys.stdin = open('input.txt')

# 중위 순회를 하며 각 노드를 층별로 배치 시키는 함수
def solution(left, root, right, depth):                     # 왼쪽 자식 노드 시작 인덱스 / 부모 노드 인덱스
                                                            # 오른쪽 자식 노드 끝 인덱스 / 트리의 레벨
    if left >= root:                                        # 리프 노드일때
        level[depth].append(in_order_li[root])              # 현재 노드의 레벨에 노드 번호 추가
        return

    solution(left, (left+root)//2, root-1, depth+1)         # 왼쪽 자식 노드 재귀 호출
    level[depth].append(in_order_li[root])                  # 부모 노드 해당하는 층에 노드 번호 추가
    solution(root+1, (root+right+1)//2, right, depth+1)     # 오른쪽 자식 노드 재귀 호출


K = int(sys.stdin.readline())                               # 트리의 레벨(깊이)
in_order_li = list(map(int, sys.stdin.readline().split()))  # 문제에서 주어진 중위순회 한 결과값
level = [[] for _ in range(K)]                              # 트리의 각 레벨별 노드 리스트

solution(0, (2**K-1)//2, 2**K-1, 0)                         # 트리 중위 순회시키는 함수 호출

for i in range(K):          # 출력
    print(*level[i])