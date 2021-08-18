#풀이1(테스트케이스 중 몇개 시간초과)
def solution(numbers):
    str_n = list(map(str, numbers))
    #버블정렬
    for i in range(len(numbers)-1, 0, -1):
        for j in range(0, i):
            #맨 앞자리수 비교해서 더 작은 값이 뒤로 오도록
            if str_n[j][0] < str_n[j+1][0]:
                str_n[j], str_n[j+1] = str_n[j+1], str_n[j]
            #맨 앞자리수가 같은 경우, 왼+오 값이랑 오+왼 값 비교하여 더 작은 값이 뒤로 오도록
            elif str_n[j][0] == str_n[j+1][0]:
                if int(str_n[j] + str_n[j+1]) < int(str_n[j+1] + str_n[j]):
                    str_n[j], str_n[j+1] = str_n[j+1], str_n[j]
    answer = ''
    for n in str_n:
        answer += n
    return answer

#풀이2(구글링)
def solution(numbers):
    str_n = list(map(str, numbers))
    #비교값(key)에 4를 곱해줘서 앞자리부터 끊김없이 비교할 수 있도록
    new_n = sorted(str_n, key=lambda x: x*4, reverse=True)

    3, 30
    30, 3

    return str(int(''.join(new_n)))

print('3' > '30')