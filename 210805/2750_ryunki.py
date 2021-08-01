N = int(input())

sortlist = []
for i in range(N):
    M = int(input())
    sortlist.append(M)

sortlist.sort()

for number in sortlist:
    print(number)
