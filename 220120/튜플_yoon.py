def solution(s):
    answer = []
    temp = sorted(list(map(str, s[2:-2].split('},{'))), key=lambda x: len(x))
    for i in range(len(temp)):
        case = list(map(int, temp[i].split(',')))
        for j in case:
            if j not in answer:
                answer.append(j)
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))