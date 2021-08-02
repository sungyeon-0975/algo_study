T = int(input())

for t in range(T):
    k = int(input())
    n = int(input())
    
    # def floor(k, n): # 재귀로 풀면 시간초과 됨
    #     if k == 0:
    #         return n
    #     people = 0
    #     for num in range(1, n+1):
    #         people += floor(k-1, num)
    #     return people

    # print(floor(k, n))

    people = [x for x in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            people[j] += people[j-1]
    
    print(people[-1])