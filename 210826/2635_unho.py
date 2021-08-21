import sys


num = int(sys.stdin.readline())

answer_cnt = 0                                          # 최대 개수를 담을 변수
answer = []                                             # 최대 개수인 숫자 리스트

n = 1                                                   
while n <= num:                                         # 두번째 숫자가 1부터 시작하여 첫번째 숫자일때까지 반복
    tmp_list = [num, n]                                 # 리스트 첫번째, 두번째 할당

    while tmp_list[-2] - tmp_list[-1] >= 0:             # 두번째 전 - 첫번째 전 한 결과가 0 이상이면 값 추가 및 개수 증가
        tmp_list.append(tmp_list[-2] - tmp_list[-1])
    
    if len(tmp_list) > answer_cnt:                      # 현재 리스트가 개수가 더 많으면 정답 변수에 저장
        answer_cnt = len(tmp_list)
        answer = tmp_list
    
    n += 1

print(answer_cnt)
print(*answer)