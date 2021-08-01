import sys                                           # input 쓰기 위한 모듈
input = sys.stdin.readline                           # 그냥 input() 쓸 때보다 속도가 확연히 빠르다

test = int(input())                                  # 테스트 케이스 갯수를 담을 test 변수
result = []                                          # 결과를 담을 result 리스트
for _ in range(test):                                # 테스트 케이스 갯수 만큼 반복 돌림
    test_list = list(map(str, input().rstrip()))     # input을 오른쪽 줄바꿈을 제외시켜서 리스트 형식으로 test_list에 넣음
    if (test_list[0] + test_list[1]) == "pu":        # 만약 test_list의 첫 번째와 두번째 글자가 pu이면
        result.append(''.join(test_list[5:]))        # test_list의 5번째부터 마지막까지 공백없이 합쳐서 result 리스트에 넣음
    elif (test_list[0] + test_list[1]) == "po":      # 만약 test_list의 첫 번째와 두번째 글자가 po이면
        if len(result) > 0:                          # result 길이가 0 이상이면
            print(result.pop())                      # result의 마지막 인덱스 값을 제외시키고 출력
        else:                                        # result 길이가 0이면
            print(-1)                                # -1 출력
    elif (test_list[0] + test_list[1]) == "si":      # 만약 test_list의 첫 번째와 두번째 글자가 si이면
        print(len(result))                           # result 길이 출력
    elif (test_list[0] + test_list[1]) == "em":      # 만약 test_list의 첫 번째와 두번째 글자가 em이면
        if len(result) == 0:                         # result 길이가 0이면 (비어 있으면)
            print(1)                                 # 1 출력
        else:                                        # result 길이가 0이 아니면 (비어 있지 않으면)
            print(0)                                 # 0 출력
    elif (test_list[0] + test_list[1]) == "to":      # 만약 test_list의 첫 번째와 두번째 글자가 to이면
        if len(result) > 0:                          # (result 길이가 0보다 크면)
           print(result[-1])                         # result의 마지막 인덱스 값 출력
        else:                                        # result 길이가 0이면
            print(-1)                                # -1 출력