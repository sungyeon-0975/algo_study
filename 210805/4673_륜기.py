def changenumber(N):    # 생성 함수
    n = N 
    msum = N
    while n > 0:
        msum += n%10
        n //= 10
    
    return msum
    
results = list(range(10001)) # 출력할 결과물

for i in range(1,10001): # 결과물에서 모든 만들어 질 수 있는 수를 제거한다.
    selfnumber = changenumber(i)

    if selfnumber < 10001:
        results [selfnumber] = False # 결과는 0부터 시작이므로 selfnumber의 인덱스 위치가 결국 selfnumber 그 자체가 된다.

for i in results :
    if i: # False와 처음 시작 0 을 제거하고 출력
        print(i)
    