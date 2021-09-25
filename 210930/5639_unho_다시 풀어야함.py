"""
시간초과
"""
# import sys
# from collections import deque
# sys.setrecursionlimit(10000)
# sys.stdin = open('input_5639.txt')


# def solution(idx, value):               # 힙에 값을 넣는 함수
#     if not tree.get(idx, 0):
#         tree[idx] = value
#         return

#     if tree[idx] > value:               # 현재 노드보다 값 크면, 왼쪽으로
#         solution(idx*2, value)
#     elif tree[idx] < value:             # 현재 노드보다 값 작으면, 오른쪽으로
#         solution(idx*2+1, value)


# def post_order(node):                   # 후위 표현식
#     if not tree.get(node, 0):
#         return

#     post_order(node*2)
#     post_order(node*2+1)
#     print(tree[node])

# arr = deque()
# tree = {}

# while True:                                     # 입력을 계속해서 받기 위함
#     try:                                        # 입력이 없으면 오류 발생하여 반복문 탈출
#         in_s = sys.stdin.readline().strip()
#         arr.append(int(in_s))
#     except:    
#         break

# tree[1] = arr.popleft()                         # 최상위루트 설정

# while arr:                                      # 힙에 값 넣음
#     value = arr.popleft()
#     solution(1, value)

# post_order(1)