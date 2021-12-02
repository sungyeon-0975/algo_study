def solution(files):
    answer = []                 # 정답 리스트
    separate_files = []         # 각 파일 하나를 이름을 규칙에 맞게 분리하여 저장할 리스트 (각 인덱스에는 [head, number, tail] 이 저장된다)

    for file in files:                                          # 파일명들 하나하나 확인
        num_start = 0                                           # 숫자 부분이 시작되는 인덱스 (파일명은 숫자가 아닌 문자로 시작하므로 0번 인덱스는 무조건 문자가 나옴 -> 숫자 시작 인덱스를 0으로 초기화 시킴)
        for i in range(len(file)):                              # 현재 파일명 인덱스로 순환
            if str(file[i]).isdigit() and not num_start:        # 현재 자릿수가 숫자인데, 그 이전에 숫자가 한번도 나온적이 없는 경우 -> 현재 인덱스 앞부분이 head
                num_start = i                                   # 현재 인덱스가 숫자 시작이므로 값 변경
                head = file[:num_start]                         # head 부분 저장

            elif num_start and not str(file[i]).isdigit():      # 앞에서 이미 숫자가 나왔었고, 현재 인덱스가 숫자가 아닌 경우 -> 현재 인덱스 앞부분이 number
                number = file[num_start:i]                      # number 변수에 저장
                tail = file[i:]                                 # 그 이후 나머지는 tail
                break                                           # 반복 종료

        else:                                                   # number 부분 뒤에 tail 이 비어있는 경우 위의 조건을 통과하지 못함 -> break 문에 걸리지 않음 -> for-else 이용하여 break 없이 통과하는 경우 실행하도록 설계
            number = file[num_start:]                           # number 변수 저장
            tail = ''                                           # 꼬리 부분 비어있는 값으로 초기화

        """ 분리된 파일명들 확인을 위한 print """
        # print(f'파일명: {file} => HEAD: {head} / NUMBER: {number} / tail: {tail}')
        # print('----------------------------------------------------------------')
        
        separate_files.append((head, number, tail))             # 분리된 파일명을 리스트에 따로 보관

    sorted_separate_files = sorted(separate_files, key=lambda x: (str(x[0]).lower(), int(x[1])))        # 분리된 파일들을 head 부분은 소문자로 바꾸어서 정렬하고 number는 int로 형변환하여 앞에 0을 제거
    answer = list(map(lambda x: x[0] + x[1] + x[2], sorted_separate_files))                             # 정답은 head, number, tail 을 모두 다시 합쳐서 정렬
    return answer


print(solution(["img12", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "IMg0010.png", "img002.png", "img01"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))