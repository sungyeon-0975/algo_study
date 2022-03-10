from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []

        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi

        counter = Counter(temp)

        if len(counter) != 0 and max(counter.values()) != 1:
            for i in counter:
                if counter[i] == max(counter.values()):
                    answer.append(''.join(i))

    return sorted(answer)
