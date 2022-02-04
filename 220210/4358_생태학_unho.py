import sys
sys.stdin = open('input.txt')

tree = {}                                               # key: 나무 이름, value: 나무의 개수

for name in sys.stdin.read().strip().split('\n'):       # 모든 입력들
    tree[name] = tree.get(name, 0) + 1                  # 딕셔너리 변수에 나무가 없으면 0으로 초기화 하고 + 1, 이미 있으면 1 증가

total = sum(tree.values())                              # 나무의 총 개수

for k in sorted(tree.keys()):                           # 나무의 종별로 반복
    print(f'{k} {tree[k] / total * 100:.4f}')