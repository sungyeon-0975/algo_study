result_list = [0, 0, 0, 0, 0]                           # 입력값을 담을 리스트를 생성
max_count = 0                                           # 최대 글자 수를 담을 max_count
for i in range(5):                                      # 5개의 문장이 들어오므로
    result_list[i] = input()                            # result_list의 각 인덱스마다 입력값을 넣어줌
    if len(result_list[i]) > max_count:                 # 만약 입력값의 길이가 max_count보다 크면
        max_count = len(result_list[i])                 # max_count에 입력값의 길이를 넣어줌

for col in range(max_count):                            # 입력값의 최대 길이만큼 for문 돎
    for row in range(len(result_list)):                 # result_list의 길이만큼 for문
        try:                                            # 일단 시도
            print(result_list[row][col], end = '')      # result_list[row][col]를 공백없이 출력 => 각 행 별로 첫 열부터 마지막 열까지 출력
        except IndexError:                              # indexerror가 나면 (해당 인덱스가 없으면)
            continue                                    # continue 시킴