def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))