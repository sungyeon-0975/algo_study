number = int(input())                   # 입력값을 int로 형변환 해서 받음

num = [0, 0]                            # 입력값을 각 자리로 따지기 위해 num 리스트를 만듦
if number < 10:                         # 만약 입력값이 10보다 작다면
    num[0] = 0                          # num[0] = 0
    num[1] = number                     # num[1] = 1 을 넣음

else:                                   # 입력값이 두 자리 숫자이면
    idx = 0                             # idx = 0으로 초기화
    for i in str(number):               # number을 str로 형변환 후 각 자릿수 for 문 돌림
        num[idx] = int(i)               # idx를 인덱스 삼아 num리스트의 idx번째 자리에 number의 각 자리를 int로 형변환 해서 넣음
        idx += 1                        # idx를 1 더해줌

result = 0                              # 반복문의 비교를 위해 최종 결과를 담을 result를 0으로 초기화
count = 0                               # 반복 횟수를 담을 count 변수 0으로 초기화
temp = [0, 0]                           # 결과를 내기 위해 temp 리스트를 0으로 초기화
while (result != number):               # result와 number가 같을 때 까지 while문 반복
    idx = 0                             # idx 0으로 초기화
    if num[0] + num[1] < 10:            # num 리스트의 0번째와 1번째 숫자의 합이 10미만이면
        temp[0] = 0;                    # temp[0]에 0을 입력
        temp[1] = num[0] + num[1]       # temp[1]에 num[0] + num[1]을 입력
    else:                               # num 리스트의 0번째와 1번째 숫자의 합이 두 자릿수이면
        for i in str(num[0] + num[1]):  # (num[0] + num[1])을 str로 형변환 시켜서 각 자릿수를 for문 돌림
            temp[idx] = int(i)          # temp의 idx번째 자리에 각 자릿수를 int로 형변환 시켜서 넣음
            idx += 1                    # idx를 1 더해줌

    num[0], num[1] = num[1], temp[1]    # num[0]에는 num[1]을 num[1]에는 temp[1](= num[0] + num[1])을 넣어줌
                                        # => num[0] + num[1]이 한 자리면 문제 없지만 두 자리 숫자이면 두 자리가 들어가기에 위의 temp 작업을 해줌
    result = num[0] * 10 + num[1]       # result에 num[0] * 10 + num[1]을 넣어줌
    count += 1                          # count를 1 더해줌
if number == 0:                         # 만약 number가 0이면 while을 돌지 않기 때문에
    count = 1                           # count = 1
print(count)                            # count 출력