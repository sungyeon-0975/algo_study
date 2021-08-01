import sys                  # input 쓰기 위한 모듈
input = sys.stdin.readline  # 그냥 input() 쓸 때보다 속도가 확연히 빠르다

x = input()                         # 입력값을 받아 x에 넣음
count = 0                           # 한수를 count할 변수
x_list = []                         # 100이상의 입력값일 시 문장의 각자릿수 비교를 위한 리스트
for i in range(1, int(x) + 1):      # 1부터 x까지 숫자를 반복시킴
    if i < 100:                     # i값이 100 미만이면 한수이므로
        count += 1                  # count를 1 증가시킴
        continue                    # 다음 반복문으로 돌림
    else:                           # i값이 100 이상이면
        x_list.append(str(i))       # x_list에 i를 문자형으로 변환해서 넣음
        if ((int(x_list[-1][0]) - int(x_list[-1][1])) == (int(x_list[-1][1]) - int(x_list[-1][2]))): # 각 숫자의 (백의자리 - 십의 자리)와 (십의 자리 - 일의 자리)가 같다면
            count += 1              # count를 1 증가시킴
print(count)                        # count 출력