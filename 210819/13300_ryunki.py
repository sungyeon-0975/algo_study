

# 남 녀를 나눠서 각각 학년별로 리스트에 저장하고 각 학년의 갯수가 최대 정원수로 나눴을 때 나머지가 없으면 그 몫을 나머지가 있으면 몫+1을 한다. 그 합들을 구하면 방의 수
def count(data):
    result = []
    for i in range(1, 7):
        if data.count(i) % max_num != 0:
            result.append((data.count(i) // max_num) + 1)
        elif data.count(i) % max_num == 0:
            result.append(data.count(i) // max_num)
    return result


total_num, max_num = map(int, input().split())

girl = []
boy = []

for i in range(total_num):
    sex, year = map(int, input().split())
    if sex == 0:
        girl.append(year)
    elif sex == 1:
        boy.append(year)

print(sum(count(boy)) + sum(count(girl)))
