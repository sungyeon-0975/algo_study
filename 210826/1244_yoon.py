import sys
input = sys.stdin.readline

def change(n): # 스위치 반대로 바꿔주는 함수
    if switch[n] == 0:
        switch[n] = 1
    else:
        switch[n] = 0

num = int(input())
switch = [0] + list(map(int, input().split())) # 인덱스 관리용 0 추가
student_num = int(input())
student = []

for s in range(student_num):
    student.append(tuple(map(int, input().split())))

for i in range(student_num):
    if student[i][0] == 1: # 남
        for si in range(1, num+1):
            if not si % student[i][1]: # 입력된 숫자의 배수 인덱스
                change(si)
    else: # 여
        idx = student[i][1]
        step = 1
        while 1 <= idx-step and idx+step <= num and switch[idx-step] == switch[idx+step]: # 길이 벗어나지 않고/양쪽 같으면
            step += 1 # 다음 step 검사용 +
        step -= 1 # 미리 더해준 step 빼줌
        for sd in range(idx-step, idx+step+1):
            change(sd)

switch = switch[1:] # 0 제거

for pr in range(0, num, 20):
    print(*switch[pr:pr+20])