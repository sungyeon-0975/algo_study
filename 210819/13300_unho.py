import sys

n, k = map(int, sys.stdin.readline().split())

student = [0] * 12                                                      # 6개 학년, 2개 성별, 학생수를 담는 리스트 0~5 여자 6~12 남자

for _ in range(n):
    s, y = map(int, sys.stdin.readline().split())
    student[(6*s) + (y-1)] += 1                                         # 0~5번 인덱스 여자 1~6학년, 6~12번 인덱스 남자 1~6학년

answer = sum(map(lambda x: x//k if not x%k else (x//k + 1), student))   # 나머지가 0 이면(인원이 최대 인원 딱 맞으면) 그냥 몫을 구함, 나머지가 존재한다면 (최대 인원 못채웠다면) 몫 + 1
print(answer)