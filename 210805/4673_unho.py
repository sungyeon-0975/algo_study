## 에라토스테네스의 체 활용

# 1부터 10,000 까지 모두 셀프넘버라고 가정
num_list = [True for _ in range(10001)]

# 1부터 시작하여 d(n) 을 실행
for idx in range(1, 10001):
    tmp = idx

    # 각 자리수 더하기
    while idx > 0:
        tmp += idx%10
        idx //= 10
    
    # 결과값이 10,000 초과시 인덱스 에러 방지
    if tmp < 10001:
        num_list[tmp] = False


for i in range(1, 10001):
    if num_list[i]:
        print(i)