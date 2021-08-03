import sys # 아직 sys 잘 모르겠는데 기솔언니가 알려줌^^
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()

for point in arr:
    print(f'{point[0]} {point[1]}')