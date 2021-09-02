result_list = []                        # 입력 값 저장 리스트
for _ in range(9):                      # 아홉 난쟁이의 키를 받기 위한 반복
    result_list.append(int(input()))    # 아홉 난쟁이 키를 result_list에 저장
result_list.sort()                      # result_list를 정렬
result_sum = sum(result_list)           # result_sum에 result_list의 합을 저장
difference = result_sum - 100           # difference에 result_sum - 100을 저장
flag = 0                                # break를 걸기 위한 flag

for i in range(len(result_list)):       # result_list 길이만큼 반복
    if flag == 1:                       # flag가 1이면
        break;                          # 반복을 빠져 나감
    for j in range(i + 1, len(result_list)):                    # i + 1부터 result_list 마지막 까지 반복 
        if (result_list[i] + result_list[j]) == difference:     # 만약 result_list의 i와 j의 합이 difference와 같으면
            result_list.remove(result_list[i])                  # 해당 값만 빼면 result_list 합이 100이 되므로 i를 제외
            result_list.remove(result_list[j - 1])              # i가 j보다 앞에 있으므로 j-1 인덱스를 제외
            flag = 1                                            # flag를 1로 만듦
            break;                                              # 반복을 빠져 나옴

for i in result_list:                   # result_list를 반복하면서
    print(i)                            # 하나씩 값을 출력