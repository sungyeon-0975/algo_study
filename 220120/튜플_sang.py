def solution(s):
    answer = []
    lst = list(s.replace('{{', '').replace('}}', '').split("},{"))

    lst.sort(key=len)
    chk = set()
    for t in lst:
        tmp = set(t.split(",")) - chk
        chk = chk | set(t.split(","))
        answer.append(int(tmp.pop()))

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{20,111},{111}}"))
