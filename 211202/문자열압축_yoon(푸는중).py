def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        temp = 0
        # while? for? len(s)//i 곱해서 단위별로 같으면 누적... 아귀찮아
        # if s[:i] == s[i:i*2]:
        #     answer = min(answer, i+1)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))