import sys
sys.stdin = open('14600_input.txt')
# input = sys.stdin.readline

K = int(input())
x, y = map(int, input().split())

arr = [[0] * 2**K for _ in range(2**K)]
arr[2**K-y][x-1] = -1
print(arr)