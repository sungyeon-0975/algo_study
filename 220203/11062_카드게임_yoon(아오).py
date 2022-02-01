import sys
sys.stdin = open('11062_input.txt')
# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    dp = [[0] for _ in range(N) for _ in range(N)]