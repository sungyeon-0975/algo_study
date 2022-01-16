def solution(numbers, target):
    answer = 0                          # 정답의 개수

    for i in range(1<<len(numbers)):    # 2^(숫자의 개수)
        tmp_sum = 0                     # 초기 합은 0
        for j in range(len(numbers)):   # 각 자릿수 만큼 반복
            if i & (1<<j):              # 현재 자리가 더하기라면
                tmp_sum += numbers[j]
            else:                       # 현재 자리가 빼기라면
                tmp_sum -= numbers[j]
        if tmp_sum == target:           # 타겟넘버를 찾으면, 정답 개수 추가
            answer += 1
    
    return answer