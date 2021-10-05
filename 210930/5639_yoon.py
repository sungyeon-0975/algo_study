import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)
sys.stdin = open('input_5639.txt')


def post_order(tree):
    if tree:
        root = tree[0]
        idx = -1
        for i in range(1, len(tree)):
            if tree[i] > root:
                idx = i
                break
        if idx == -1:
            post_order(tree[1:])
        else:
            post_order(tree[1:idx])
            post_order(tree[idx:])
        print(root)


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

post_order(pre_order)