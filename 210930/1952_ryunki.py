import sys

sys.stdin = open('input_1952.txt')

for test in range(1, 1 + int(input())):
    day, month, three, year = map(int, input().split())
    data = [0] + list(map(int, input().split())) # 인덱스를 맞춰준다
    temp = [0] * 13 # 맞춘 인덱스에 따른 최소값 누적합 저장
    for i in range(1, 13):
        temp[i] = min(data[i] * day, month) + temp[i - 1] # 일별과 한달치를 비교

        if i > 2: # 3달 치를 계산하려면 3번째 달부터만 계산할 수 있다.
            temp[i] = min(temp[i], three + temp[i - 3]) # 3달 더하기 그전까지의 누적합을 더한 것과 현재 달까지의 누적합을 비교

    answer = min(temp[12], year) # 1년과 마지막 달까지의 누적합 비교
    print('#{} {}'.format(test, answer))
