####### 1호 2호 3호 4호
# 3층 :  1   5  15  35
# 2층 :  1   4  10  20
# 1층 :  1   3  6   10
# 0층 :  1   2  3   4

# k층 n호 = k-1층 n호 + k층 n-1호

# k-1층 n호 = sum(1~n) + sum(1~n-1) + sum(1)

def my_sum(k, n):
    if n == 1:
        return 1                                # 1호는 무조건 1 출력
    if k == 0:
        return n                                # 0층은 무조건 n 출력
    
    return my_sum(k - 1, n) + my_sum(k, n - 1)  # k층 n호 = k-1층 n호 + k층 n-1호

test_case = int(input())                        # 테스트 케이스 갯수 입력받음

for _ in range(test_case):                      # 테스트 케이스 갯수만큼 for문 돌림
    k = int(input())                            # 층, input 받은 문장을 정수로 치환
    n = int(input())                            # 호, input 받은 문장을 정수로 치환


  ### 재귀가 시간초과 됐는데, 반복문으로 못 풀겠어서 구글링 해옴  
# t = int(input())

# for _ in range(t):  
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for k in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력