def solution(array, commands):
    result = []
    for idx in commands:
        result.append(sorted(array[idx[0] - 1 : idx[1]])[idx[2]-1]) # commands의 각 인덱스마다 첫번째 인덱스부터 두번째 인덱스 까지 슬라이싱 한 것을 정렬한 뒤, commands의 세 번째 인덱스 - 1번째 인덱스 값을 담음
    return result