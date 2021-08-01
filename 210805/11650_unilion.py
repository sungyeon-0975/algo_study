import sys                  # input 쓰기 위한 모듈
input = sys.stdin.readline  # 그냥 input() 쓸 때보다 속도가 확연히 빠르다

test = int(input())         # test_case 갯수를 input 받음
dot_list = []               # 입력를 담을 dot_list 생성

for _ in range(test):       # 테스트 케이스 갯수만큼 반복
    dot_list.append(list(map(int, sys.stdin.readline().split())))       # input을 공백기준으로 받고 int로 치환해서 dot_list에 추가
dot_list = sorted(dot_list, key=lambda x : (x[0], x[1]))                # dot_list를 람다식으로 0번째 인덱스 기준, 1번째 인덱스 기준으로 정렬

for do in dot_list:             # dot_list 각각을 뽑음
        print(do[0], do[1])     # 0번째와 1번째 인덱스 값을 출력