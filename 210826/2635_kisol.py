import sys

input = sys.stdin.readline

num1 = int(input())
max_len = 0

for num2 in range(num1 // 2, num1 + 1):  # 두 번째 숫자(첫 번째 숫자의 중간부터~첫 번째 숫자까지)
    temp = [num1, num2]
    idx = 0

    # 두 번째 숫자에 따른 전체 숫자리스트 생성
    while temp[idx] - temp[idx + 1] >= 0:
        temp.append(temp[idx] - temp[idx + 1])
        idx += 1

    # 최대 숫자 개수 구하기
    if max_len < len(temp):
        max_len = len(temp)
        ans = temp[:]  # 최대일 경우, temp리스트를 복사해옴

print(max_len)
print(*ans)  # 최종 저장돼있는 최대 숫자 개수의 숫자 리스트 출력
