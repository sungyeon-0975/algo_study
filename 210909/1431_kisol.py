import sys

# 29200 KB / 84 ms
# input = sys.stdin.readline
sys.stdin = open('input_1431.txt')

input()  # 제출할 때 삭제
N = int(input())
s = sorted([input() for _ in range(N)])
s_sum = {key: 0 for key in s}  # 각각의 숫자합 딕셔너리

# s_sum에 숫자합 담기
for chars in s:
    for char in chars:
        if char.isdigit():
            s_sum[chars] += int(char)

for i in range(N - 1, 0, -1):  # 끝 포인트
    for j in range(i):
        if len(s[j]) > len(s[j + 1]):
            s[j], s[j + 1] = s[j + 1], s[j]
        elif len(s[j]) == len(s[j + 1]):
            if s_sum[s[j]] > s_sum[s[j + 1]]:
                s[j], s[j + 1] = s[j + 1], s[j]

for serial in s:
    print(serial)
