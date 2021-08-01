test = int(input())                     # test에 test case 갯수를 입력 받음

result_list = []                        # 각 테스트 케이스의 값을 담을 result_list 생성
for i in range(test):                   # test 갯수만큼 for문을 돌림
    result_list.append(int(input()))    # result_list에 테스트 케이스를 int로 형변환해서 담음

result = []                             # 정렬돼서 결과 출력할 값을 담을 result 리스트 생성
result = sorted(result_list)            # result_list를 오름차순으로 정렬해서 result 리스트에 담음
for i in result:                        # result를 하나씩 for문 돌림
    print(i)                            # result의 값을 하나씩 출력