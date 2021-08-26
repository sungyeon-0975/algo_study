import sys

input = sys.stdin.readline

N = int(input())
switch = [0] + list(map(int, input().split()))  # idx번호와 스위치 번호 매치하여 생성
T = int(input())

for _ in range(T):
    gen, num = map(int, input().split())

    # 남학생인 경우, 번호의 배수 스위치 on/off
    if gen == 1:
        for i in range(1, N + 1):  # 모든 스위치 번호(1~N)
            if i % num == 0:
                switch[i] = 1 if switch[i] == 0 else 0
    # 여학생의 경우, 번호 기준으로 대칭되는 최대 구간 on/off
    else:
        start, end = num, num + 1
        i = 1
        while num - i > 0 and num + i < len(switch):
            if switch[num - i] == switch[num + i]:
                start, end = num - i, num + i + 1
                i += 1
            else:
                break
        for i in range(start, end):
            switch[i] = 1 if switch[i] == 0 else 0

# 20개 숫자씩 출력
for i in range(1, len(switch) - 1):
    if i % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end=' ')
print(switch[len(switch) - 1])