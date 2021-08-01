test = int(input())               # 테스트 케이스 갯수만큼 입력받아서 int로 형변환

for i in range(test):             # 테스트 케이스 갯수 만큼 for문 돌림
    ox = input()                  # OX를 입력받아 ox 변수에 저장

    result = 0                    # 결과값을 담을 변수 0으로 초기화
    count = 0                     # O가 연속된 갯수만큼 세줄 변수 0으로 초기화
    for o in ox:                  # ox의 각 단어를 for문 돌림
        if o == "O":              # 만약 o가 O를 받는다면
            count += 1            # count를 1 증가시킴
        else:                     # o가 X를 받으면
            count = 0             # count를 0으로 초기화
        result += count           # result에 count 수 만큼 더해줌
    print(result)                 # result 출력
