from itertools import permutations


def solution(expression):
    answer = 0
    exp = ["-", "+", "*"]
    nums = list(map(int, expression.replace(
        '-', ' ').replace('+', ' ').replace('*', ' ').split()))
    exps = list(filter(lambda x: x in exp, expression))

    for ex in permutations(exp):
        tmp = 0
        for e in ex:
            break

        answer = max(answer, abs(tmp))
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
