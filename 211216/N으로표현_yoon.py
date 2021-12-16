def solution(N, number):
    answer = -1
    case = [[int(str(N) * i)] for i in range(1, 9)]
    # print(case)

    if [number] in case:
        return case.index([number]) + 1

    for i in range(1, 8):
        temp = set()
        for j in range(i):
            for num1 in case[j]:
                for num2 in case[i-j-1]:
                    temp.add(num1 + num2)
                    temp.add(num1 - num2)
                    temp.add(num1 * num2)
                    if num2 != 0:
                        temp.add(num1 // num2)
        case[i].extend(temp)
        # print(case)
        if number in case[i]:
            answer = i + 1
            break
    return answer

print(solution(5, 12))
print(solution(2, 11))