import sys

sys.stdin = open('input_2477.txt')

fruit_per = int(input())

data = []
for i in range(6):
    direction, cm = map(int, input().split())
    data.append(cm)

large = 0
small = 0

for i in range(6):
    temp = data[i] * data[(i + 1) % 6]
    if large < temp:
        large = temp
        small = data[(i + 3) % 6] * data[(i + 4) % 6]

print(fruit_per * (large - small))
