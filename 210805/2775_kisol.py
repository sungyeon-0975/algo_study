T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    people = [list(range(1, n + 1))]
    if k != 0:
        for stage in range(k + 1):
            people.append([])
            for room in range(n):
                people[stage].append(sum(people[stage - 1][0:room + 1]))
    result = people[stage][room]

    print(result)