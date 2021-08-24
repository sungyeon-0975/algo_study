'''
1. 조건과 연산을 줄이기 위해 스위치 꺼짐 0 을 -1로 변경하여 저장
2. 인덱스 혼동을 줄이기 위해 0번 인덱스에 허위 값 추가
'''


import sys

switch_num = int(sys.stdin.readline())
switch_list = [2] + list(map(lambda x: -1 if x == '0' else int(x), sys.stdin.readline().split()))     # 스위치 숫자와 인덱스를 맞추기 위해 0번 인덱스에 인위적인 값 추가, -1:꺼짐 / 1:켜짐

student_num = int(sys.stdin.readline())
student_list = [list(map(int, sys.stdin.readline().split())) for _ in range(student_num)]

for gen, num in student_list:
    if gen == 1:                        # 남자
        idx = num
        while idx <= switch_num:        # 스위치 인덱스 초과하기 전까지
            switch_list[idx] *= -1      # 스위치 전환
            idx += num                  # 배수
    
    else:                               # 여자
        switch_list[num] *= -1          # 입력받은 숫자 전환
        left, right = num-1, num+1      # 왼쪽 오른쪽 인덱스 설정

        while 1 <= left and right <= switch_num and switch_list[left] == switch_list[right]: # 범위 안에 있고, 왼쪽 오른쪽이 같을때
            switch_list[left] *= -1     # 스위치 전환
            switch_list[right] *= -1
            left -= 1                   # 왼쪽 오른쪽 이동
            right += 1

for idx in range(1, len(switch_list)):                      # 0번 인덱스는 인덱스 맞추기 용으로 출력하지 않는다
    print(0 if switch_list[idx] == -1 else 1, end=' ')      # 값이 -1 이면 0으로 출력 
    if not idx%20:                                          # 20개 출력하고 나면 
        print()