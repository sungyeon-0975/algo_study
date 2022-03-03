import sys
sys.stdin = open('2512_input.txt')
# input = sys.stdin.readline

N = int(input())
request = list(map(int, input().split()))
total = int(input())
low, high = 0, max(request)

while low <= high:
    mid = (low + high) // 2
    temp = 0
    for num in request:
        if num >= mid:
            temp += mid
        else:
            temp += num
    if temp <= total:
        low = mid + 1
    else:
        high = mid - 1
print(high)
