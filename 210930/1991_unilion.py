import sys
input = sys.stdin.readline

# 29200KB	76ms

# 전위 순회 (V -> L -> R)
def pre_order(node):
    for i in range(N):
        if node_list[i][0] == node:
            print(node_list[i][0], end = '')
            pre_order(node_list[i][1])
            pre_order(node_list[i][2])
            continue
                

# 중위 순회 (L -> V -> R)
def in_order(node):
    for i in range(N):
        if node_list[i][0] == node:
            in_order(node_list[i][1])
            print(node_list[i][0], end = '')
            in_order(node_list[i][2])
            continue

# 후위 순회 (L -> R -> V)
def post_order(node):
    for i in range(N):
        if node_list[i][0] == node:
            post_order(node_list[i][1])
            post_order(node_list[i][2])
            print(node_list[i][0], end = '')
            continue


N = int(input())
node_list = [input().split() for _ in range(N)]

pre_order(node_list[0][0])
print()

in_order(node_list[0][0])
print()

post_order(node_list[0][0])