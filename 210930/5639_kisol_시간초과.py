import sys


# KB / ms
# input = sys.stdin.readline
'''
[입력이 있는 만큼만 받아오기]
1. try except 구문 활용
2. sys.stdin.readlines() 활용 - 파일의 끝까지 한번에 가져오고 이걸 한줄씩 가져와서 쓰는 방식
'''
sys.stdin = open('input_5639.txt')
sys.setrecursionlimit(10**6)


def post_order(node):
    if node:
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(node)


# 이진 탐색 조건에 따라 트리 생성 (전위 순회가 트리 들어오는 숫자랑 같음)
def make_tree(node, parent):
    if node < parent:
        if tree[parent][0] == 0:
            tree[parent][0] = node
        else:
            make_tree(node, tree[parent][0])
    else:
        if tree[parent][1] == 0:
            tree[parent][1] = node
        else:
            make_tree(node, tree[parent][1])


pre_order = []
# 입력이 있는 만큼만 받아오기
while True:
    try:
        pre_order.append(int(input()))
    except (EOFError, ValueError):
        break

root = pre_order[0]
tree = {key: [0, 0] for key in pre_order}

for i in range(1, len(pre_order)):
    make_tree(pre_order[i], pre_order[0])

post_order(pre_order[0])
