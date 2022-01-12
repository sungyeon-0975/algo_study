import sys
sys.stdin = open('17141_input.txt')
# input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
# 2에 바이러스 놓을 수 있고 1은 벽, 0은 빈 칸(퍼지기 가능)
# 바이러스는 상하좌우로 1초 걸려 퍼짐

# 바이러스 놓을 수 있는 위치 comb로 구하고 모든 경우의 수에 대해 BFS 진행?