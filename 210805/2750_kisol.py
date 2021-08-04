T = int(input())
num = []

for i in range(T):
    num.append(int(input()))

num.sort()
for n in num:
    print(n)