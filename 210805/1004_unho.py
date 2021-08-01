import sys
import math


'''
##1차 생각
#원리
출발점과 도착점이 각 행성계의 중점과의 거리를 구한다.
이 거리가 행성계의 반지름 안에 들어간다면 속한다고 표시

#상세
1.행성의 x,y 와 출발점 sx, sy 도착점 dx, dy 의 거리를 각자 구함
출발점과 행성 : (abs(sx-x)**2 + abs(sy-y)**2)**0.5   <- 두 점의 거리

2.위의 계산결과가 반지름 r 보다 작으면 행성계 구역 안에 속함

3.출발점이 속한 구역을 나타낼 리스트 생성하고 속하는 행성의 인덱스를 추가 (위 과정을 도착점도 동일하게 진행)

4. 두 리스트 합집합에서 교집합 부분을 빼고, 요소의 갯수가 정답
(위 과정은 반례 1번을 방지하기 위함)

# 예상되는 반례
1. 출발점과 도착점이 하나의 큰 행성계 구역 안에 모두 들어가는 경우
'''



test_case = int(sys.stdin.readline())


for _ in range(test_case):
    start_end = list(map(int, sys.stdin.readline().split())) # 출발점과 도착점 좌표 / 순서대로 출발점 x, y 도착점 x, y

    planetary_num = int(sys.stdin.readline()) # 행성계 개수
    planetary_list = [list(map(int, sys.stdin.readline().split())) for _ in range(planetary_num)] # 행성계 리스트, 각 요소가 리스트임 / 순서대로 행성계 x, y, r

    # 시작점과 도착점이 각 속한 행성의 인덱스를 담을 집합
    start_include = set()
    end_include = set()

    # 각 행성계의 정보를 가져옴
    for planetary in planetary_list:
        # 출발점과 도착점의 행셩계와의 거리 구하기 위함 (x, y 의 거리 차이)
        start_dx = abs(planetary[0] - start_end[0])
        start_dy = abs(planetary[1] - start_end[1])
        end_dx = abs(planetary[0] - start_end[2])
        end_dy = abs(planetary[1] - start_end[3])

        # 피타고라의 정리 이용하여 각 점의 직선거리를 구함
        start_distance = (start_dx**2 + start_dy**2)**0.5
        end_distance = (end_dx**2 + end_dy**2)**0.5

        # 출발점과 도착점이 반지름 보다 짧다면(행성계 안에 속한다면), 변수에 저장
        if planetary[2] > start_distance: start_include.add(planetary_list.index(planetary))
        if planetary[2] > end_distance: end_include.add(planetary_list.index(planetary))

    # 출발점과 도착점이 함께 속한 행성계는 제거 (같은 행성계 안에 속하면 경계를 지날 필요가 없음)
    union_include = start_include.union(end_include)
    intersection_include = start_include.intersection(end_include)
    answer = union_include - intersection_include

    # 요소의 개수 - 지나야 하는 경계 수
    print(len(answer))