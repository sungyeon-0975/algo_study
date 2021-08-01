result_list = []                        # 결과를 담을 빈 리스트 생성
for _ in range(10000):                  # 10000번 반복 돌리면서
    result_list.append(1)               # result_list에 1을 담음

for number in range(1, 10001):          # 숫자 1 ~ 10000까지 반복을 돌림
    result = number                     # result에 해당 숫자 넣음
    for number_string in str(number):   # 해당 숫자를 문자화해서 각 자릿수를 반복 돌림
        result += int(number_string)    # reuslt에 각 자리수를 추가로 더해줌
    try:                                
        result_list[result - 1] = 0     # result_list의 (result - 1)번째 인덱스 값을 0으로 해줌
    except IndexError:                  # 인덱스 에러날 시
        continue                        # 계속 진행함

count = 1                               # 결과를 출력할 count 변수 1로 초기화
for idx in result_list:                 # result_list의 값들을 돌면서
    if idx == 1:                        # 해당 값이 1이면
        print(count)                    # count 출력 (해당 값이 1이면 count(해당 인덱스 + 1)가 곧 self number)
    count += 1                          # (count를 1 증가시킴)