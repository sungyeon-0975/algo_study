A = int(input())
B = int(input())
C = int(input())

res = A * B * C
result = []
for char in str(res):
    result.append(char)

for number in range(10):
    print (result.count(str(number)))