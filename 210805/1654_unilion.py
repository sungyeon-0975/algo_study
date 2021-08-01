import sys
input = sys.stdin.readline

current, need = input().split(" ")              # 현재 가지고 있는 랜선의 갯수와 필요한 랜선의 갯수를 입력 받음

current_list = []                               # 현재 가지고 있는 랜선의 길이들을 담을 리스트
for cur in range(int(current)):                 # 현재 가지고 있는 랜선 갯수 만큼 반복
    current_list.append(int(input().rstrip()))  # current_list에 현재 가지고 있는 랜선의 길이들을 담음
start = 1                                       # 비교할 랜선 길이, start를 1로 초기화
end = max(current_list)                         # 비교할 랜선 길이, end를 현재 가지고 있는 랜선의 길이 중 가장 긴 길이로 초기화
while start <= end:                             # start가 end보다 작거나 같을 때 까지 반복
    line = 0                                    # mid로 랜선을 나눌 시, 나오는 랜선의 갯수를 0으로 초기화
    mid = (start + end) // 2                    # start와 end의 중간값을 mid로 저장
    for i in current_list:                      # 현재 가지고 있는 랜선의 길이를 반복 시킴
        line += i // mid                        # line에 현재 랜선 길이에 start와 end의 중간값으로 나눈 몫을 더해나감
    print(line >= int(need))
    if line >= int(need):                       # 다 더한 line값이 필요한 갯수 보다 많으면 (길이를 더 늘려도 되므로)
        start = mid + 1                         # start를 mid + 1로 만듦
    else:                                       # 다 더한 line 값이 필요한 갯수 보다 적으면 (길이를 줄여야 하므로)
        end = mid - 1                           # end를 mid - 1 로 만듦
    print(f'start = {start} , end = {end}, line = {line}, need = {int(need)}')
print(end)                                      # end가 start보다 작으면 필요한 라인 갯수에 맞는 라인의 최대 길이를 알 수 있으므로, 최종 결과인 end를 출력
