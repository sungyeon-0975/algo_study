#시간 초과
import sys                                          # input 쓰기 위한 모듈
input = sys.stdin.readline                          # 그냥 input() 쓸 때보다 속도가 확연히 빠르다

test = input()                                      # 입력값을 활용 안 하기에 받기만 하는 용

a = list(map(int, input().split()))                 # 입력을 공백 기준으로 나눠서 int로 형변환 후 리스트로 받아 a에 넣음
b = list(map(int, input().split()))                 # 입력을 공백 기준으로 나눠서 int로 형변환 후 리스트로 받아 b에 넣음
result = []                                         # 결과를 담을 result 리스트
for i in a:                                         # a의 값들을 돌리면서
    if i not in b:                                  # b에 해당 값이 없으면
        result.append(i)                            # result에 추가

for i in b:                                         # b의 값들을 돌리면서
    if i not in a:                                  # a에 해당 값이 없으면
        result.append(i)                            # result에 추가

print (len(result))                                 # result의 길이 출력


""" #구글링해서 참조
test = input() # 입력값

a = set(map(int, input().split())) # a집합의 입력값을 set으로 받음
b = set(map(int, input().split())) # b집합의 입력값을 set으로 받음
print (len(a-b) + len(b-a))        # set은 차집합이 가능하기에 각각을 뺀 길이의 합을 출력
"""