import sys
sys.stdin = open('12015_input.txt')
# input = sys.stdin.readline

# 143064KB / 4888ms

A = int(input())
numbers = [0] + list(map(int, input().split()))
ans = [0]

for num in numbers:
    if ans[-1] < num:
        ans.append(num)
    else:
        left = 0
        right = len(ans)
        while left < right:
            mid = (left + right) // 2
            if ans[mid] < num:
                left = mid + 1
            else:
                right = mid
        ans[right] = num

print(len(ans)-1)