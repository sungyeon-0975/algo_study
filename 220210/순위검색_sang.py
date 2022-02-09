def solution(info, query):
    answer = []

    info_table = []

    for i in info:
        info_table.append(list(map(str, i.split())))

    info_table.sort(key=lambda x: (x[4]))

    for q in query:
        cond = list(map(str, q.split()))
        cnt = 0

        for info in info_table:
            if int(cond[7]) > int(info[4]):
                continue
            if cond[0] != info[0] and cond[0] != '-':
                continue
            if cond[2] != info[1] and cond[2] != '-':
                continue
            if cond[4] != info[2] and cond[4] != '-':
                continue
            if cond[6] != info[3] and cond[6] != '-':
                continue

            cnt += 1
        answer.append(cnt)

    return answer
