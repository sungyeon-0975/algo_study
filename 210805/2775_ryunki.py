t = int(input())

for repeat in range(t):
    k = int(input())
    n = int(input())
    People = list(range(1,n+1))

    for floor in range(k):
        for room in range(1,n):
            People[room] += People[room-1]
        # print(People)
    print(People[-1])
