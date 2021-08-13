def solution(array, commands):
    answer = []

    for e in commands:                      # command 요소 반복
        tmp_list = array[e[0]-1 : e[1]]     # 리스트 슬라이싱
        tmp_list.sort()                     # 리스트 정렬
        answer.append(tmp_list[e[2]-1])     # 해당 인덱스 요소 정답 리스트에 할당
    
    return answer

print(solution([1,5,2,6,3,7,4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))