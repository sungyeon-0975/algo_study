import sys
input = sys.stdin.readline

N, capacity = map(int, input().split())
students = [[0, 0] for _ in range(6)]
rooms = 0

for _ in range(N):
    gender, grade = map(int, input().split())
    students[grade-1][gender] += 1

for grade in range(6):
    for gender in range(2):
        rooms += students[grade][gender] // capacity
        if students[grade][gender] % capacity != 0:
            rooms += 1

print(rooms)