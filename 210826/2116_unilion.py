import sys
input = sys.stdin.readline

dice = int(input())                                             # 주사위 갯수
dice_list = []                                                  # 주사위 상태 담을 리스트
for _ in range(dice):                                           # 주사위 갯수만큼 반복
    dice_list.append(list(map(int, input().split())))           # 주사위 상태를 dice_list에 담음

result_list = []                                                # 옆면의 합을 담을 result_list
for uppper_number in range(1, 7):                               # 1번 주사위의 윗면 = upper_number
    result = 0                                                  # 옆면의 합을 담을 변수
    idx = 0                                                     # idx에 현재 주사위 위치를 담음
    while idx < dice:                                           # 다이스 갯수만큼 while 반복
        for i in range(6):                                      # 주사위의 6면을 다 봄
            if dice_list[idx][i] == uppper_number:              # 만약 현재 idx번 째 주사위의 i번 째 면이 위쪽 주사위면과 같으면
                if i == 0:                                      # 0번 째 면이면
                    result += max(dice_list[idx][1], dice_list[idx][2], dice_list[idx][3], dice_list[idx][4]) # 1, 2, 3, 4번째 면 중 최댓값을 result에 더함
                    uppper_number = dice_list[idx][5]           # 윗 면의 숫자를 0번과 짝인 5번째 면 숫자로 바꿈
                elif i == 1:                                    # 1번 째 면이면
                    result += max(dice_list[idx][0], dice_list[idx][2], dice_list[idx][4], dice_list[idx][5]) # 0, 2, 4, 5번째 면 중 최댓값을 result에 더함
                    uppper_number = dice_list[idx][3]           # 윗 면의 숫자를 1번과 짝인 3번째 면 숫자로 바꿈
                elif i == 2:                                    # 2번 째 면이면
                    result += max(dice_list[idx][0], dice_list[idx][1], dice_list[idx][3], dice_list[idx][5]) # 0, 1, 3, 5번째 면 중 최댓값을 result에 더함
                    uppper_number = dice_list[idx][4]           # 윗 면의 숫자를 2번과 짝인 4번째 면 숫자로 바꿈
                elif i == 3:                                    # 3번 째 면이면
                    result += max(dice_list[idx][0], dice_list[idx][2], dice_list[idx][4], dice_list[idx][5]) # 0, 2, 4, 5번째 면 중 최댓값을 result에 더함
                    uppper_number = dice_list[idx][1]           # 윗 면의 숫자를 3번과 짝인 1번째 면 숫자로 바꿈
                elif i == 4:                                    # 4번 째 면이면
                    result += max(dice_list[idx][0], dice_list[idx][1], dice_list[idx][3], dice_list[idx][5]) # 0, 1, 3, 5번째 면 중 최댓값을 result에 더함
                    uppper_number = dice_list[idx][2]           # 윗 면의 숫자를 4번과 짝인 2번째 면 숫자로 바꿈
                elif i == 5:                                    # 5번 째 면이면
                    result += max(dice_list[idx][1], dice_list[idx][2], dice_list[idx][3], dice_list[idx][4]) # 1, 2, 3, 4번째 면 중 최댓값을 result에 더함
                    uppper_number = dice_list[idx][0]           # 윗 면의 숫자를 5번과 짝인 0번째 면 숫자로 바꿈
                break                                           # 윗면과 같은 것을 찾았으면 더 찾을 필요 없으므로 break
        idx += 1                                                # 다음 주사위로 넘김
        
    result_list.append(result)                                  # result_list에 각 윗면당 result를 담음
print(max(result_list))                                         # 해당 결과 리스트 중 가장 큰 값을 출력