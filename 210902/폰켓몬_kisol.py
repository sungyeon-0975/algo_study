def solution(nums):
    new_nums = set(nums)
    if len(new_nums) >= len(nums) // 2:
        return len(nums) // 2
    return len(new_nums)


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
