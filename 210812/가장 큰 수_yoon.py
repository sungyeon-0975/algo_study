def solution(numbers):
    numbers = list(map(str, numbers))
    comp = []
    for num in numbers:
        num_3 = num*3
        comp.append([num_3[:3], num])
    comp.sort(key = lambda x : int(x[0]), reverse=True)
    
    answer = ''
    for idx in range(len(numbers)):
        answer += comp[idx][1]
    return answer

print(solution([6, 10, 2])) # 예시 케이스는 통과, 전체 케이스 중 4개만 통과