def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i, j, k = map(int, commands[idx])
        arr = sorted(array[i-1:j]) # slicing 하려면 i-1부터 시작
        answer.append(arr[k-1]) # 'k번째' 숫자니까 idx로는 k-1
    return answer

print(solution([1, 5, 2, 6, 3, 7], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))