import itertools


def solution(input_orders, course):
    answer = []
    orders = [0] * len(input_orders)

    for i in range(len(input_orders)):
        orders[i] = sorted(list(input_orders[i]))

    for num in course:
        combs_dict = dict()
        for order in orders:
            combs = list(itertools.combinations(order, num))
            for comb in combs:
                comb = ''.join(comb)
                if comb in combs_dict:
                    combs_dict[comb] += 1
                else:
                    combs_dict[comb] = 1
        if combs_dict.values():
            max_val = max(combs_dict.values())
            if max_val >= 2:  # 2.89ms => 1.79ms
                for key, val in combs_dict.items():
                    if val == max_val:
                        answer.append(key)
        else: break
        # for key, val in combs_dict.items():
        #     if val >= 2 and val == max_val:
        #         answer.append(key)

    answer.sort()
    return answer