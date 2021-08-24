first_value = int(input())              # 처음 값 입력 받음

half = first_value // 2                 # 처음의 절반 값 구함
result = 0                              # 결과값

for i in range(half, first_value + 1):  # 처음 수에서 절반 이하 값을 빼면 3번째 수가 무조건 2번째 수보다 큼. => 절반부터 처음 수까지 검사
    temp_first = first_value            # temp_first에 first_value를 넣어줌 // 계산될 처음 수
    temp_second = i                     # temp_second에 half부터 처음 수 까지 현재 i 값을 넣어줌 // 계산될 두번째 수
    temp_current = 0                    # temp_current를 0으로 초기화 // 계산될 세번째 수(현재 수)

    temp_list = []                      # temp_list를 초기화 // 지금까지 temp값들을 넣어줌
    cnt = 0                             # cnt를 0으로 초기화 // len(temp_list)와 같음

    while temp_current >= 0:            # temp_current가 양수일동안 동작
        cnt += 1                        # cnt를 1 더해줌
        temp_list.append(temp_first)    # temp_list에 temp_first 추가
        temp_current = temp_first - temp_second # temp_current에 temp_first - temp_second 한 값을 넣어줌
        temp_first = temp_second        # temp_first에 temp_second를 넣어줌
        temp_second = temp_current      # temp_second에 temp_current를 넣어줌 (한 줄로 안 한 이유는 보기 편하려고)
        if temp_current < 0:            # temp_current가 음수가 되면
            temp_list.append(temp_first)    # temp_list에 temp_first를 추가
            cnt += 1                        # cnt를 1 더해줌

    if result < cnt:                    # result가 cnt보다 작으면
        result = cnt                    # result를 cnt로 바꿔줌
        result_list = temp_list[:]      # result_lsit에 temp_list를 복사함 
print(result)                           # result 출력
print(*result_list)                     # result_list를 언패킹해서 리스트 없애고 출력