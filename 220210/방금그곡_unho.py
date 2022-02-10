def solution(m, musicinfos):
    def separate(s):                                    # 문자열 음을 리스트 형태로 나누어주는 함수
        result = []                                     # 리스트로 변형된 음
        
        for c in s:
            if c == '#':                                # 현재 인덱스가 # 이라면, 이전에 기록한 음에 # 이 붙어야하므로
                result.append(f'{result.pop()}{c}')     # 마지막 요소를 꺼낸 후 뒤에 붙여서 다시 추가
            else:                                       # 현재 문자가 # 이 아니라면 반환할 리스트에 항목 추가
                result.append(c)

        return result                                   # 리스트 형태로 반환

    def make_table(pattern):                            # KMP 알고리즘에 사용할 패턴의 테이블 구하는 함수
        table = [0] * len(pattern)                      # 테이블 값 초기화
        j = 0                                           # 접두사 인덱스
        for i in range(1, len(pattern)):                
            if j > 0 and pattern[i] != pattern[j]:      # 문자가 일치하지 않으면, 접두사 인덱스 0 할당 
                j = 0
            
            if pattern[j] == pattern[i]:                # 문자가 일치하면, 인덱스 증가 및 테이블에 기록
                j += 1
                table[i] = j

        return table                                    # 테이블 반환

    def KMP(s, pattern):                                # KMP 알고리즘
        j = 0
        for i in range(len(s)):
            while j > 0 and s[i] != pattern[j]:         # 문자가 일치하지 않으면, 테이블에 입력된 인덱스로 이동
                j = table[j-1]
            
            if s[i] == pattern[j]:                      # 문자가 일치하면
                if j >= len(pattern) - 1:               # 패턴과 모두 일치하면 찾았으므로 종료
                    return True
                else:                                   # 인덱스 증가
                    j += 1
        return False                                    # 패턴이 포함되지 않으므로 False 반환
    
    musics = []                         # 음악 정보들 (멜로디, 제목)
    answers = []                        # 정답 리스트
    max_len = 0                         # 정답인 음악의 재생 시간

    separate_m = separate(list(m))      # 문자열인 패턴을 리스트 형태로 변환
    table = make_table(separate_m)      # 패턴의 테이블 만들기

    for info in musicinfos:
        start, end, title, tmp_melody = info.split(',')     # 음악 재생 시작 시간, 음악을 끈 시간, 제목, 멜로디

        play_time = (int(end[:2]) - int(start[:2]))*60 + (int(end[3:]) - int(start[3:]))    # 재생 시간(분)
        melody = separate(list(tmp_melody))     # 문자열인 멜로디를 리스트로 변환

        tmp, idx = [], 0                        # 재생시간 길이만큼의 멜로디를 저장할 리스트, 멜로디 인덱스
        while play_time > 0:                    # 재생시간이 남아 있으면 반복
            if idx >= len(melody):              # 멜로디가 재생시간보다 잛으면 멜로디 인덱스 0으로 옮김
                idx = 0

            tmp.append(melody[idx])             # 멜로디 추가

            idx += 1
            play_time -= 1
        musics.append((tmp, title))             # 음악 정보 저장
            
    for melody, title in musics:                # 가공된 데이터들 반복
        if KMP(melody, separate_m):             # 일치하는 노래라면
            if len(melody) > max_len:           # 최대 길이로 재생된 음악인 경우
                answers.clear()                 # 이전 음악 기록 제거
            max_len = len(melody)               # 최대 길이 갱신
            answers.append((len(melody), title))    # 정답에 추가

    if not answers:             # 출력
        return '(None)'
    else:
        return answers[0][1]


print(solution('ABCDEFG', ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution('CC#BCC#BCC#BCC#B', ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#", ["03:00,03:08,FOO,CC#B"]))