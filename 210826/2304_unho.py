'''
1. 기둥들을 1차원 배열 리스트에 할당한다.
2. 리스트를 높이를 기준으로 내림차순으로 정렬
3. 기둥을 기준으로 왼쪽 오른쪽으로 다음 높은 기둥을 구한다.
4. 그 기둥과 인덱스와 떨어진만큼 거리를 곱하여 넓이를 구한다.

시간 - 80 ms
'''

import sys



n = int(sys.stdin.readline())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

n_list.sort(key=lambda x: x[1], reverse=True)               # 기둥 리스트를 높이를 기준으로 내림차순으로 정렬
print(n_list)

center_idx = left_idx = right_idx = n_list[0][0]            # 가장 높은 기둥의 인덱스 (값 고정) / 왼쪽에 높은 기둥 나타나면 인덱스 갱신 / 오른쪽에 높은 기둥 나타나면 인덱스 갱신
answer += n_list[0][1]                                      # 가장 높은 기둥은 1칸 * 높이 의 넓이를 가지므로 초기 넓이로 설정해준다.

for idx in range(1, len(n_list)):                           # 기둥 리스트에서 맨 앞에 가장 높은 기둥은 넓이를 구했으므로 다음 기둥부터 반복
    tmp_idx = n_list[idx][0]                                # 현재 기둥의 인덱스 (위치)
    tmp_height = n_list[idx][1]                             # 현재 기둥의 높이

    if tmp_idx > center_idx and tmp_idx > right_idx:        # 현재 기둥의 위치가 가장 높은 기둥보다 크고, 오른쪽 인덱스보다 클때
        answer += (tmp_idx - right_idx) * (tmp_height)      # (현재 위치 - 오른쪽 인덱스) * 높이
        right_idx = tmp_idx                                 # 오른쪽 인덱스 = 현재 기둥의 인덱스
        
    elif tmp_idx < center_idx and tmp_idx < left_idx:       # 현재 기둥의 위치가 가장 높은 기둥보다 작고, 왼쪽 인덱스보다 작을때
        answer += (left_idx - tmp_idx) * (tmp_height)       # (현재 위치 - 왼쪽 인덱스) * 높이
        left_idx = tmp_idx                                  # 왼쪽 인덱스 = 현재 기둥의 인덱스

print(answer)