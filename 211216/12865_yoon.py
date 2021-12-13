import sys
sys.stdin = open('12865_input.txt')
# input = sys.stdin.readline

N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]