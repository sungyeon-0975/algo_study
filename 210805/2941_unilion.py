croatia = input()               # 크로아티아 문자를 입력받아 croatia 변수에 넣음

croatia_list = []               # croatia문자의 각 단어를 담을 croatia_list를 생성
for croa in croatia:            # croatia의 각 단어를 반복시킴
    croatia_list.append(croa)   # 각 단어를 croatia_list에 담음

count = 0                       # 크로아티아 문자가 있을 시 그 다음 단어는 건너 뛰기 위한 count
croa_count = 0                  # 크로아티아 단어 count
idx = -1                        # crotia_list의 index를 따지기 위한 idx 변수
for croa in croatia_list:       # 크로아티아의 단어 수 만큼 반복을 돌림
    idx += 1                    # idx에 1을 더해줌
    if count >= 1:              # count가 1 이상이면 => croatia 문자가 나오면
        count -= 1              # count를 1 빼줌
        continue                # 다음 반복 돌림

    try:
        if croa == 'c':                             # 단어가 c일 때
            if croatia_list[idx + 1] == '=' \
                or  croatia_list[idx + 1] == '-':   # 그 다음 단어가 '='이나 '-'이면 => 끝에 \ 을 붙인 이유는 줄이 길어져서 밑으로 내리 위해 씀
                count = 1                           # count를 1로 만듦

        elif croa == 'd':                           # 단어가 d일 때
            if croatia_list[idx + 1] == '-':        # 그 다음 단어가 '-' 이면
                count = 1                           # count를 1로 만듦
            elif croatia_list[idx + 1] == 'z':      # 그 다음 단어가 'z' 이고
                if croatia_list[idx + 2] == '=':    # 그 다다음 단어가 '=' 이면
                    count = 2                       # count를 2로 만듦 => 반복을 두 번 건너 뛰어야 하기 때문임
        
        elif croa == 'l':                           # 단어가 l일 때
            if croatia_list[idx + 1] == 'j':        # 그 다음 단어가 'j' 이면
                count = 1                           # count를 1로 만듦

        elif croa == 'n':                           # 단어가 n일 때
            if croatia_list[idx + 1] == 'j':        # 그 다음 단어가 'j' 이면
                count = 1                           # count를 1로 만듦

        elif croa == 's':                           # 단어가 s일 때
            if croatia_list[idx + 1] == '=':        # 그 다음 단어가 '=' 이면
                count = 1                           # count를 1로 만듦

        elif croa == 'z':                           # 단어가 z일 때
            if croatia_list[idx + 1] == '=':        # 그 다음 단어가 '=' 이면
                count = 1                           # count를 1로 만듦

        else:                                       # 그 외에는
            count = 0                               # count를 0으로 만듦
        
        croa_count += 1                             # croa_count를 1 증가시킴

    except IndexError:                              # 만약 인덱스 에러가 나면   
        croa_count += 1                             # croa_count를 1 증가시키고 (마지막 단어이거나 마지막 이전 단어가 d일 때)
        continue                                    # 반복을 진행함

print(croa_count)                                   # 크로아 단어 갯수인 croa_count를 출력시킴