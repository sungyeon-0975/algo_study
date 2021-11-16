"""
pre --> CLR
in ---> LCR -> 루트 노드를 기준으로 왼쪽 오른쪽으로 나누어짐
post -> LRC -> 분할하였을때 항상 가장 오른쪽 인덱스가 루트노드가 됨

1. post 이용하여 루트노드의 값을 구한다
2. in 에서 루트노드를 기준으로 왼쪽과 오른쪽으로 나누어 분할정복
2-1. in 에서 가장 왼쪽의 노드값을 알아내 post 에서도 왼쪽 오른쪽 분할시킨다.
3. 재귀
"""


"""
Python
    Timeover

PyPy3
    Memory - 339 MB
    Time - 2.976 s
"""

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)


def get_tree(in_start, in_end, root_idx):       # in_order 에서 시작 인덱스 / 끝 인덱스 / 루트 인덱스
    root = post_order_li[root_idx]              # 루트 노드의 값
    idx = in_order_li.index(root)               # in 에서 루트 노드의 인덱스 값

    left_start = in_start                       # 루트 기준 왼쪽 시작 인덱스 / 끝 인덱스
    left_end = idx-1                    

    right_start = idx+1                         # 루트 기준 오른쪽 시작 인덱스 / 끝 인덱스
    right_end = in_end

    print(root, end=' ')                        # 루트 값 출력 (pre-order 인 경우 루트 노드부터 출력하므로)

    if left_end < left_start and right_start <= right_end:          # 왼쪽 자식 노드는 없고, 오른쪽 자식 노드는 있을때
        get_tree(right_start, right_end, root_idx-1)                # 오른쪽 자식 노드 재귀 호출

    elif right_end < right_start and left_start <= left_end:        # 오른쪽 자식 노드는 없고, 왼쪽 자식 노드는 있을때
        get_tree(left_start, left_end, root_idx-1)                  # 왼쪽 자식 노드 재귀 호출

    elif left_start <= left_end and right_start <= right_end:       # 왼쪽 자식 노드와 오른쪽 자식 노드가 모두 있을때
        right = post_order_li.index(in_order_li[right_start])       # post-order 에서 오른쪽 자식 노드 시작지점을 찾아냄

        get_tree(left_start, left_end, right-1)                     # 왼쪽 자식 노드 재귀 호출
        get_tree(right_start, right_end, root_idx-1)                # 오른쪽 자식 노드 재귀 호출


N = int(sys.stdin.readline())
in_order_li = list(map(int, sys.stdin.readline().split()))
post_order_li = list(map(int, sys.stdin.readline().split()))    # 입력

get_tree(0, N-1, N-1)       # 시작 인덱스 / 끝 인덱스 / 루트 인덱스