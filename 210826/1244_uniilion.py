switch_case = int(input())                                   # switch_case에 스위치 갯수 입력 받음
switch_status = list(map(int,input().split()))               # switch_status에 스위치 상태 입력 받음
students = int(input())                                      # students에 학생 수 입력받음
student_list = []                                            # student_list를 초기화
for _ in range(students):                                    # 학생 수 만큼 반복
    student_list.append(list(map(int, input().split())))     # 성별 및 스위치 번호를 리스트 형식으로 student_list에 담음

for student in student_list:                                                                        # student_list에서 하나씩 꺼냄
    if student[0] == 1:                                                                             # 남자라면
        for switch in range(1, switch_case + 1):                                                    # 1부터 switch 갯수까지 반복
            if not (switch % student[1]):                                                           # 만약 switch가 학생 스위치 번호와 나누어 떨어지면
                switch_status[switch - 1] = int(not switch_status[switch - 1])                      # switch 번째 스위치의 상태를 반전

    elif student[0] == 2:                                                                           # 여자라면
        switch_status[student[1] - 1] = int(not switch_status[student[1] - 1])                      # 학생 스위치 번호 째 스위치 상태를 반전

        for i in range(1, switch_case + 1):                                                         # 1부터 switch 갯수까지 반복
            if (((student[1] - 1 - i) >= 0) and ((student[1] - 1 + i) <= switch_case - 1))\
                and (switch_status[student[1] - 1 - i] == switch_status[student[1] - 1 + i]):       # 인덱스가 0이상 switch_case - 1 이하 이면서 학생번호 기준 좌우 대칭이면
                switch_status[student[1] - 1 - i] = int(not switch_status[student[1] - 1 - i])      # 해당 스위치 상태를 반전
                switch_status[student[1] - 1 + i] = int(not switch_status[student[1] - 1 + i])      # 해당 스위치 상태를 반전
            else:       # 좌우 대칭이 아니거나 인덱스가 벗어나면
                break   # 반복문 탈출

for i in range(5):                                                      # 스위치 최대 100개, 한 줄 최대 20개 => 최대 5번 반복
    print(' '.join(map(str, switch_status[20 * i : 20 * (i + 1)])))     # 슬라이싱으로 20개씩 잘라서 출력
    if len(switch_status) >= (20 * (i + 1)):                            # 만약 switch 갯수가 20 * i개 이상이면
        pass    # 계속 하고
    else:       # switch 갯수가 20 * i개 미만이면
        break   # 반복문 탈출