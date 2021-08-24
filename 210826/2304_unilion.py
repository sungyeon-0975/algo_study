import sys
input = sys.stdin.readline

pillar = int(input())                                       # 기둥의 갯수 입력 받음

pillar_list = []                                            # 기둥의 위치와 높이를 받을 리스트 
for _ in range(pillar):                                     # 기둥 갯수만큼 반복
    pillar_list.append(list(map(int, input().split())))     # 기둥의 위치와 높이를 int로 변환해서 리스트로 담아서 pillar_list에 추가함
pillar_list = sorted(pillar_list, key = lambda x:x[0])      # pillar_list를 x[0]을 기준으로 오름차순 정렬

current_pillar = pillar_list[0][0]                          # 현재 기둥의 위치를 담을 변수에 0번째 인덱스 위치를 넣음
current_height = pillar_list[0][1]                          # 현재 기둥의 높이를 담을 변수에 0번째 인덱스 높이를 넣음

last_pillar = pillar_list[-1][0]                            # 마지막 기둥의 위치를 담을 변수에 마지막 인덱스 위치를 넣음
last_height = pillar_list[-1][1]                            # 마지막 기둥의 높이를 담을 변수에 마지막 인덱스 높이를 넣음

max_pillar = pillar_list[0][0]                              # 최대 높이의 기둥 위치를 담을 변수에 0번째 인덱스 위치를 넣음
max_height = pillar_list[0][1]                              # 최대 높이의 기둥 높이를 담을 변수에 0번째 인덱스 높이를 넣음
result = 0                                                  # 결과를 담을 변수
max_idx = 0                                                 # 최대 높이를 담는 인덱스

# 최대 높이인 순간 구하기
for i in range(pillar):                                     # 기둥 갯수 만큼 반복
    if max_height <= pillar_list[i][1]:                     # 현재 인덱스의 기둥 높이가 최대 높이보다 크거나 같다면
        max_idx = i                                         # max_idx를 현재 인덱스로 교체

        if max_height < pillar_list[i][1]:                  # 현재 인덱스의 기둥 높이가 최대 높이보다 크다면
            max_pillar = pillar_list[i][0]                  # 현재 인덱스의 기둥 위치를 최대 높이의 기둥 위치로 바꿈
            max_height = pillar_list[i][1]                  # 현재 인덱스의 기둥 높이를 최대 높이의 기둥 높이로 바꿈
        
# 올라갈 때
for i in range(max_idx + 1):                                # 최대 높이의 기둥 인덱스까지 반복
    if current_height < pillar_list[i][1]:                  # 현재 인덱스의 기둥 높이가 현재 기둥 높이보다 크다면
        row = pillar_list[i][0] - current_pillar            # row에 현재 인덱스의 기둥 위치와 현재 기둥의 위치를 뺀 값을 넣음
        col = current_height                                # col에 현재 기둥의 높이를 담음
        result += (row * col)                               # result에 row * col의 결과값을 더해줌
        current_pillar = pillar_list[i][0]                  # 현재 기둥의 위치에 현재 인덱스의 기둥 위치를 넣음
        current_height = pillar_list[i][1]                  # 현재 높이에 현재 인덱스의 기둥 높이를 담음

# 최대 높이
max_row = pillar_list[max_idx][0] - max_pillar + 1          # max_row에 최대 높이의 마지막 인덱스 위치에서 최대 높이의 처음 인덱스 위치를 뺀 값에 1을 더해줌
result += max_row * max_height                              # result에 max_row * max_height 결과 값을 더해줌
current_height = max_height                                 # 현재 높이에 최대 높이를 담아줌
current_pillar = pillar_list[max_idx][0]                    # 현재 기둥의 위치에 최대 높이의 마지막 인덱스 위치를 담아줌

# 내려갈 때
for idx in range(max_idx + 1, pillar):                      # (최대 높이의 마지막 인덱스 + 1)부터 기둥 갯수까지 인덱스 반복
    
    if idx == pillar - 1:                                   # 현재 인덱스가 기둥갯수 - 1과 같다면 (마지막 인덱스라면)
        row = last_pillar - current_pillar                  # row에 마지막 기둥 위치에서 현재 기둥 위치를 뺀 값을 담음
        col = last_height                                   # col에 마지막 기둥 높이를 담음
        result += (row * col)                               # result에 (row * col)한 값을 담음
        break                                               # for문 탈출
    
    temp_list = pillar_list[idx:pillar]                     # temp_list에 현재 인덱스부터 마지막 인덱스까지 슬라이싱해서 담음
    max_col = temp_list[0][1]                               # max_col에 temp_list의 첫번째 인덱스 높이를 담음
    for temp in temp_list:                                  # temp_list를 하나씩 순환 => 남은 기둥 중 최대 높이 값 구하기
        if max_col < temp[1]:                               # max_col이 temp_list의 현재 인덱스 높이 값보다 작으면
            max_col = temp[1]                               # max_col에 temp_list의 현재 인덱스 높이 값을 담음

    # 기둥 높이가 마지막 기둥 높이보다 큰 경우에만 돌아야 오목하게 들어간 부분이 없음
    if (max_col == pillar_list[idx][1]) and (pillar_list[idx][1] > last_height):     # 현재 인덱스의 높이 값이 최대 높이값과 같고 마지막 기둥의 높이보다 크면
        row = pillar_list[idx][0] - current_pillar          # row에 현재 인덱스의 기둥 위치에서 현재 기둥 위치를 뺀 값을 담음
        col = pillar_list[idx][1]                           # col에 현재 인덱스의 높이 값을 담음
        result += (row * col)                               # result에 (row * col)한 값을 더해줌
        current_pillar = pillar_list[idx][0]                # 현재 기둥의 위치를 현재 인덱스의 기둥 위치로 바꿔줌
        current_height = pillar_list[idx][1]                # 현재 기둥의 높이를 현재 인덱스의 기둥 높이로 바꿔줌
        
if pillar == 1:                                             # 만약 기둥이 1개라면
    print(pillar_list[0][1])                                # 첫번째 인덱스의 기둥 높이를 담음

else:                                                       # 기둥이 2개 이상이면
    print(result)                                           # 최종 result값을 반환