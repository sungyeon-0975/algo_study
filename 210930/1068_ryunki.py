"""

29200KB, 64ms

"""

import sys

sys.stdin = open('input_1068.txt')


def Delete(delete):  # 재귀로 해당 노드 부터 밑에 노드 삭제
    for i in tree[delete]:
        Delete(i)
    tree[delete] = 0


N = int(input())
tree = [[] for _ in range(N)]
for i, v in enumerate(map(int, input().split())):  # 좌표값이 결국엔 자식노드 번호
    if v == -1:  # 부모노드인 0은 제외
        continue
    tree[v].append(i)  # 해당 부모노드의 위치에 자식노드 번호 삽입
# print(tree) # 결과적으로 부모노드 인덱스에 자식노드 번호가 들어있는 트리 완성
delete = int(input())  # 지울 번호

Delete(delete)  # 지운다

# print(tree)
answer = tree.count([])+tree.count([delete]) # 아예 아래 자식이 없던 경우나 delete 번호를 자식으로 두고 있던 경우에는 자식노드가 없다
print(answer)

