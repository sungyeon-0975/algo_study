import sys
sys.stdin = open('2573_input.txt')
# input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

# 0 아닌 것들 갯수 / 상하좌우로 검사
