import sys

sys.stdin = open('input_13458.txt')

for test in range(int(input())):
    N = int(input())
    people = list(map(int, input().split()))
    B, C = map(int, input().split())
    answer = 0
    # 총감독관 제외 부감독 제외를 한반씩 생각해보자
    for i in people:
        i -= B # 총감독관 수를 빼고나면
        temp = 1 # 감독관 수는 한명
        if i > 0: # 그럼에도 반에 사람이 남아있다면
            temp += i // C # 부감독 감시 인원가능 수만큼 나눈 수를 더한다.
            if i % C != 0: # 마지막에도 나눠떨어지지 않는 수가 있다면
                temp += 1 # 한명 더 더해준다
        answer+=temp # 한반의 최종 감독수를 더한다

    print(answer)
