from collections import Counter

def solution(nums):
    d = Counter(nums)
    n = len(nums)//2
    if len(d.keys()) <= n:
        return len(d.keys())
    else:
        return n

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))