import sys

sys.stdin = open('input.txt')


N = int(input())
data = []

for i in range(N):
    position, high = list(map(int, input().split()))
    data.append((position, high))

data.sort()
left_high = data[0][1]
left_position = data[0][0]
left_width = left_position - 0
left_sum = 0
for i in range(1, len(data)):
    if left_high <= data[i][1]:
        left_width = data[i][0] - left_position
        left_sum += (left_width * left_high)
        left_high = data[i][1]
        left_position = data[i][0]

data.reverse()
right_high = data[0][1]
right_position = data[0][0]
right_sum = 0
for i in range(1, len(data)):
    if right_high < data[i][1]:
        right_width = right_position - data[i][0]
        right_sum += (right_width * right_high)
        right_high = data[i][1]
        right_position = data[i][0]


answer = left_sum + right_sum

if left_position == right_position:
    answer += left_high * 1

print(answer)
