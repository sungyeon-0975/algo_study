test_case = int(input())                # 테스트 케이스 갯수만큼 입력받아서 int로 형변환

for _ in range(test_case):              # 테스트 케이스 갯수 만큼 for문 돌림
    x = list(input().split(" "))        #  " "을 기준으로 리스트로 입력 값을 받음
    a = int(x[0])                       # 첫 번째 입력값을 int로 형변환 후 a에 입력
    b = int(x[1])                       # 두 번째 입력값을 int로 형변환 후 b에 입력
    print(a + b)                        # a + b의 값 출력