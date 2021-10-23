word = input()  # 입력
cnt = 0     # 갯수 세는 변수
temp = ""   # 빈 문자열로 초기화
flag = 0    # 반복문 빠져나올 변수
for a in ['A', 'E', 'I', 'O', 'U']:     # A, E, I, O, U 하나씩 순회
    temp += a           # temp에 a를 추가
    cnt += 1            # cnt를 1 추가해줌
    if temp == word:    # temp랑 word랑 같으면
        flag = 1        # flag 1로 갱신
    if flag == 1:       # flag가 1이면
        break           # 반복문 탈출
    for b in ['A', 'E', 'I', 'O', 'U']:     # A, E, I, O, U 하나씩 순회
        temp += b           # temp에 b를 추가
        cnt += 1            # cnt를 1 추가해줌
        if temp == word:    # temp랑 word랑 같으면
            flag = 1        # flag 1로 갱신
        if flag == 1:       # flag가 1이면
            break           # 반복문 탈출
        for c in ['A', 'E', 'I', 'O', 'U']:     # A, E, I, O, U 하나씩 순회
            temp += c           # temp에 c를 추가
            cnt += 1            # cnt를 1 추가해줌
            if temp == word:    # temp랑 word랑 같으면
                flag = 1        # flag 1로 갱신
            if flag == 1:       # flag가 1이면
                break           # 반복문 탈출
            for d in ['A', 'E', 'I', 'O', 'U']:     # A, E, I, O, U 하나씩 순회
                temp += d           # temp에 d를 추가
                cnt += 1            # cnt를 1 추가해줌
                if temp == word:    # temp랑 word랑 같으면
                    flag = 1        # flag 1로 갱신
                if flag == 1:       # flag가 1이면
                    break           # 반복문 탈출
                for e in ['A', 'E', 'I', 'O', 'U']:     # A, E, I, O, U 하나씩 순회
                    temp += e           # temp에 e를 추가
                    cnt += 1            # cnt를 1 추가해줌
                    if temp == word:    # temp랑 word랑 같으면
                        flag = 1        # flag 1로 갱신
                    if flag == 1:       # flag가 1이면
                        break           # 반복문 탈출
                    temp = temp[:-1]    # temp에서 마지막 글자를 빼줌
                if flag == 1:       # flag가 1이면
                    break           # 반복문 탈출
                temp = temp[:-1]    # temp에서 마지막 글자를 빼줌
            if flag == 1:       # flag가 1이면
                break           # 반복문 탈출
            temp = temp[:-1]    # temp에서 마지막 글자를 빼줌
        if flag == 1:       # flag가 1이면
            break           # 반복문 탈출
        temp = temp[:-1]    # temp에서 마지막 글자를 빼줌
    if flag == 1:       # flag가 1이면
        break           # 반복문 탈출
    temp = temp[:-1]    # temp에서 마지막 글자를 빼줌
print(cnt)  # cnt 출력