'''
80ms
'''
def find_leaf(idx):
    global cnt
    if childs[idx]:
        for i in childs[idx]:
            find_leaf(i)
    elif idx != -1:
        cnt += 1


if __name__ == "__main__":
    n = int(input())
    info = list(map(int, input().split()))
    ignore = int(input())
    childs = [[] for _ in range(n+1)]

    for idx, parent in enumerate(info):
        if idx != ignore:
            childs[parent].append(idx)
    cnt = 0
    find_leaf(-1)
    print(cnt)