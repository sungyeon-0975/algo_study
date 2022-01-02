from itertools import permutations

n = int(input())
lst = list(map(int, input().split()))
ans = 0

for per in permutations(lst):  # 순서섞기
    tmp = 0                    # 임시 합계
    for i in range(n-1):
        tmp += abs(per[i]-per[i+1])
    ans = max(ans, tmp)        # 정답 초기화

print(ans)
