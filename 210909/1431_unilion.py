"""
시리얼 번호 A-Z, 0-9
1. 길이가 짧은 것이 먼저 온다.
2. 길이 같을 시, 숫자 합이 작은 것이 먼저 온다.
3. 길이와 숫자합이 같으면, 숫자와 알파벳 사전순 나열

기타의 갯수 N
"""

# 입력
N = int(input())
serial_dict = {}
for _ in range(N):
    i = input()
    serial_dict[i] = len(i)
serial_dict = sorted(serial_dict.items(), key=(lambda x:x[1]))  # 시리얼 번호를 길이별로 정렬

count_list = [[] for i in range(serial_dict[-1][1] + 1)]        # 이차원 리스트로 빈 리스트를 (가장 긴 길이 + 1)만큼 생성

for i in range(len(serial_dict)):                               # 시리얼 갯수만큼 반복
    count_list[serial_dict[i][1]].append((serial_dict[i][0]))   # countt_list의 시리얼 길이 인덱스에 해당 시리얼 추가

for i in range(len(count_list)):                # count_list 길이만큼 반복
    if len(count_list[i]) > 1:                  # 만약 시리얼 갯수가 2개 이상인 곳이 있으면
        count_list[i].sort()                    # 해당 시리얼들을 정렬
        temp_list = []                          # temp_list라는 빈 리스트 생성
        for j in count_list[i]:                 # 해당 시리얼들을 반복
            len_i = 0                           # len_i를 0으로 초기화
            for str_i in j:                     # 시리얼 번호를 한 글자씩 반복
                if str_i.isdigit():             # 해당 글자가 숫자이면
                        len_i += int(str_i)     # len_i에 해당 숫자를 더함
            temp_list.append(len_i)             # temp_list에 해당 시리얼의 숫자 합을 저장

        temp_dict = {}                                              # temp_dict이라는 딕셔너리 생성
        for m in range(len(temp_list)):                             # 숫자합이 저장된 tmep_list 길이만큼 반복
            temp_dict[count_list[i][m]] = temp_list[m]              # temp_dict의 key로 해당 시리얼 번호를, value로 해당 숫자 합을 저장
        temp_dict = sorted(temp_dict.items(), key=(lambda x:x[1]))  # temp_dict을 value 기준으로 정렬
        
        for m in range(len(temp_dict)):                             # temp_dict 길이만큼 반복
            count_list[i][m] = temp_dict[m][0]                      # count_list의 같은 시리얼 길이가 2개 이상인 곳에 정렬된 것을 하나씩 다시 넣음

for m in range(len(count_list)):                                    # count_list 길이만큼 반복
    if len(count_list[m]) > 0:                                      # 길이가 0 초과면
        for n in range(len(count_list[m])):                         # 해당 시리얼 갯수 만큼 반복
            print(count_list[m][n])                                 # 하나씩 출력