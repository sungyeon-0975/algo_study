def solution(array, commands):
    answer = []
    for i in commands:
        new_array = array[i[0] - 1:i[1]]
        new_array.sort()
        answer.append(new_array[i[2] - 1])
    return answer

# 인덱스 자르고 그 리스트를 정렬한 후에 정렬한 리스트에서 해당 번호에 해당하는 수 출력