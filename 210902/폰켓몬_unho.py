def solution(nums):
    if len(nums)/2 > len(set(nums)): return len(set(nums))
    else: return len(nums)//2


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))