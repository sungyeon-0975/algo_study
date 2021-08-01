import sys

k, n = map(int, sys.stdin.readline().split())
num_list = [int(sys.stdin.readline()) for _ in range(k)]
high, low = sum(num_list)//n, 1

while low <= high:
    length = (high+low)//2
    # 각 랜선들을 최대 길이만큼 잘랐을때 몇개가 나오는지 answer에 저장
    cnt = sum([n//length for n in num_list])

    if cnt < n:
        high = length - 1
    else:
        low = length + 1
        answer = length

print(answer)