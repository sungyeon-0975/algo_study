a = int(input())                        # 첫 번째 입력값을 정수로 형변환 후 a에 입력
b = int(input())                        # 두 번째 입력값을 정수로 형변환 후 b에 입력
c = int(input())                        # 세 번째 입력값을 정수로 형변환 후 c에 입력

result = a * b * c                      # a * b* c의 값을 result에 입력
result_list = [0 for x in range(0,10)]  # 인덱스 0 ~ 9를 0으로 채운리스트를 result_list에 담음
for i in str(result):                   # for문을 돌리기 위해 result의 값을 str로 형변환 시켜서 각 문자형 숫자를 for 문 돌림
    result_list[int(i)] += 1            # 문자형 숫자를 다시 정수로 변환 후 해당 인덱스 자리를 + 1 시킴

for results in result_list:             # result의 0 ~ 9 까지 각 숫자의 갯수를 담음 result_list를 for문으로 돌림
    print(results)                      # 0 ~ 9까지 각각의 숫자 갯수를 출력