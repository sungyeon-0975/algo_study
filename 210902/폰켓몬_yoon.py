def solution(nums):
    answer = 0
    
    N = len(nums) // 2
    M = len(set(nums))
    
    if N > M:
        answer = M
    else:
        answer = N
    
    return answer