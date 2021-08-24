# 어펜드 쓰지말자.. 어펜드 시간 많이 잡아먹는다... 차라리 리스트를 초기화 하자 런타임 에러 싫어요 틀렸습니다 싫어요...
def change(num):
    if data[num] == 0:
        data[num] = 1
    else:
        data[num] = 0
    return


N = int(input())
data = [0] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    sex, number = map(int, input().split())

    # boy
    if sex == 1:
        for i in range(number, N + 1, number): # 배수만큼 바꿔준다...
            change(i)

    # girl
    else:
        change(number)  # 일단 기준점 변환
        for j in range(number): # 넘버까지만 보면 된다..
            if number + j > N or number - j < 1: break # 범위넘어가면 멈춰
            if data[number + j] == data[number - j]: # 같으면 바꿔
                change(number + j)
                change(number - j)
            else:
                break # 서로 다른 경우도 멈춰

for i in range(1, N + 1):
    print(data[i], end=' ')
    if i % 20 == 0: # 20번째 인덱스면 줄바꿈
        print()
