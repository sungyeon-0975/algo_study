students, room = map(int, input().split())
student_list = []
result = 0
for _ in range(students):
    student_list.append(list(map(int, input().split()))) # 학생 정보 리스트에 2차원 배열로 담기
#student_list.sort(key=lambda x:(x[0], x[1])) # 성별, 학년별 정렬

student_sort_list = [[], []] #[[0 : 여성] [1 : 남성]]
for i in range(2): # 성별, 학년별 정렬 위한 리스트
    for _ in range(6):
        student_sort_list[i].append(0)
for i in student_list:
    student_sort_list[i[0]][i[1] - 1] += 1 # 해당 성별 학년 인덱스에 + 1

for student_sort in student_sort_list:
    for student in student_sort:
        if student % room:
            result += student // room + 1 # 나눠 떨어지지 않으면 몫 + 1 더하기
        else:
            result += student // room   # 딱 나눠 떨어지면 그대로 더하기
print(result)