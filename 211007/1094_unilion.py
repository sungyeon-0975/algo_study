"""
29200KB, 76ms
문제 이해를 잘 못 했어서 구글링을 했습니다.
괜찮은 풀이법이 있길래 한 번 읽고서 안 보고 짜봤습니다.
"""

stick = [64, 32, 16, 8, 4, 2, 1]    # 막대기 종류는 다음의 8개 밖에 없다.
x = int(input())
result = 0
for s in stick:     # 스틱 한 종류씩 꺼내면서
    if x >= s:      # 원하는 값보다 작을 때
        result += 1 # result + 1 해준 뒤
        x -= s      # x값을 s만큼 빼줌
    
    if x == 0:      # x가 0이면
        break       # 종료
print(result)