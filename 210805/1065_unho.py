import sys

number = int(sys.stdin.readline())
answer = 0

for n in range(1, number+1):
    tmp = []        # 숫자의 각 자리수를 담을 임시 리스트 변수
    sign = True     # 한수의 여부를 판별하는 bool 변수 (초기에 한수라고 설정)

    # 숫자의 각 자릿수를 담음
    while n > 0:
        tmp.append(n%10)
        n //= 10
    
    # 숫자가 두자릿수 이상일때만, (한자리수는 모두 한수임)
    if len(tmp) > 1:
        gap = tmp[0] - tmp[1]   # 첫째자리와 둘째자리의 차이를 구함
        
        for i in range(1, len(tmp)-1):  # 둘째자리와 그 다음 자릿수의 차이를 구하기 위함
            if gap != tmp[i] - tmp[i+1]:    # 등차가 아닐때 sign 변수를 False 로 설정
                sign = False
                break
    
    # 한수라면 정답에 +1
    if sign == True:
        answer += 1

print(answer)