# 84ms
# 구글링 참고해서 다시 품
# 물이 새는 곳의 갯수 : N
# 테이프의 길이 : L
N, L = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()   # 정렬 안 해주면 틀림

result = 1              # 테이프 최소 갯수
current = N_list[0]     # 현재 물새는 곳 위치
future = current + L    # 테이프가 최대 커버할 수 있는 위치

for n in N_list:        # 리스트를 하나씩 순회
    if n < future:      # 커버 가능 위치가 현재 값보다 크면
        continue        # 다음 순회
    result += 1         # 테이프 개수 + 1
    current = n         # 현재 위치를 갱신
    future = current + L    # 커버할 수 있는 위치를 재정의
print(result)