from itertools import permutations


def solution(expression):
    answer = 0
    exp = ["-", "+", "*"]
    for ex in permutations(exp):
        e1, e2 = ex[0], ex[1]
        lst = []
        for i in expression.split(e1):
            l = [f"({j})" for j in i.split(e2)]
            lst.append(f"({e2.join(l)})")
        tmp = eval(e1.join(lst))
        answer = max(answer, abs(tmp))
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
