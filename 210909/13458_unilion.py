"""
912ms

N : 시험장
i번 시험장 응시자 수 : Ai
총감독관 감시 응시자수 : B명
부감독관 감시 응시자수 : C명
한 시험장 -> 총 : 1명, 부 : 여러 명
필요한 감독관 최소값

input
시험장 개수 : N
응시자 수 : Ai
감독관 수  : B, C
"""

# 입력
N = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for i in range(len(Ai)):                            # 시험장 수 만큼 반복
    if Ai[i] <= B:                                  # 총 감독관이 감시할 수 인원 수 이하면
        result += 1                                 # 결과에 1을 더함
    else:                                           # 총 감독관이 감시할 수 인원보다 많으면
        if (Ai[i] - B) % C:                         # (응시자 - 총감독관 감시자수)가 부감독관 감시자수와 나누어 떨어지지 않으면
            result += 1 + (Ai[i] - B) // C + 1      # 1 + (응시자 - 총감독관 감시자수)에서 부감독관 감시자수 나눈 몫 + 1
        else:                                       # 나누어 떨어지면
            result += 1 + (Ai[i] - B) // C          # 1 + (응시자 - 총감독관 감시자수)에서 부감독관 감시자수 나눈 몫을 더함

print(result)