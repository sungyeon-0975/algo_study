def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        temp = ''
        cnt = 1
        for j in range(1, len(s)//i + 2):
            if s[i*(j-1):i*j] == s[i*j:i*(j+1)]:
                cnt += 1
            else:
                if cnt != 1:
                    temp += s[i*(j-1):i*j] + str(cnt)
                else:
                    temp += s[i*(j-1):i*j]
                cnt = 1
        answer = min(answer, len(temp))
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))