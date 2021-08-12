def solution(numbers):
    numbers = list(map(str, numbers))
    comp = []
    for num in numbers:
        num_3 = num * 3
        comp.append([num_3, num])
    
    comp.sort(key = lambda x : x[0], reverse=True) # int로 안 감싸줘도 str는 사전식으로 검사하기 때문에 잘 나옴
    
    answer = ''
    for idx in range(len(numbers)):
        answer += comp[idx][1]
    return str(int(answer)) # 0000 처리해주기 위해 int로 한번 감싸고 str

print(solution([6, 10, 2]))