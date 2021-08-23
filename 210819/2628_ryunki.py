

# 가로와 세로로 자를 번호를 저장하고 각 번호들의 차이 중에서 가장 큰 값들이 결국 가장 큰 사각형의 넓이
def search(data):
    result = []
    for i in range(1, len(data)):
        result.append(data[i] - data[i - 1])
    return result


row, column = map(int, input().split())

number = int(input())

zero = []
one = []
for i in range(number):
    a, b = map(int, input().split())
    if a == 0:
        zero.append(b)
    elif a == 1:
        one.append(b)

zero.sort()
zero = [0] + zero + [column]
one.sort()
one = [0] + one + [row]

print(max(search(zero)) * max(search(one)))
