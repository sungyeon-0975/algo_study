import sys
# input = sys.stdin.readline
sys.stdin = open('input_1068.txt')

'''
29200KB / 72ms
'''


def dfs(erase):
    global parent
    parent[erase] = -2
    for i in range(N):
        if parent[i] == erase:
            dfs(i)

N = int(input())
parent = list(map(int, input().split()))
E = int(input())
cnt = 0
dfs(E)

for i in range(N):
    if parent[i] != -2 and i not in parent: # 삭제된 노드가 아니고 나를 부모로 하는 노드가 없다면(자식이 없다면)
        cnt +=  1

print(cnt)