from itertools import combinations


def solution(relation):
    answer = []
    l = len(relation[0])
    key = [i for i in range(l)]

    for i in range(1, l+1):
        for comb in combinations(key, i):
            lst = []
            for rel in relation:
                student = [rel[c] for c in comb]
                if student in lst:
                    break
                else:
                    lst.append(student)

            else:
                for ans in answer:
                    if not set(ans) - set(comb):
                        break
                else:
                    answer.append(comb)

    return len(answer)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
      "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
