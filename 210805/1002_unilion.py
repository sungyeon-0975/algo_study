import sys                                          # input 쓰기 위한 모듈
input = sys.stdin.readline                          # 그냥 input() 쓸 때보다 속도가 확연히 빠르다

test = int(input())                                 # 테스트 케이스 갯수, 입력값을 int로 변환해서 test 변수에 넣음

for _ in range(test):                               # test 만큼 반복 돌림
    start = list(map(int,input().split()))          # 입력값을 공백기준으로 나눠서 int형식으로 나눠서 리스트에 저장함
    planets = int(input())                          # 행성 갯수, 입력값을 int로 변환해서 planets 변수에 넣음
    count = 0                                       # 행성계 진입 / 이탈 횟수
    for _ in range(planets):                        # 행성 갯수만큼 for문 돌림
        x, y, r = list(map(int,input().split()))    # 각 행성의 x,y좌표와 반지름 r을 입력 받음
        if (((x-start[0])**2 + (y-start[1])**2)**0.5 <= r) and (((x-start[2])**2 + (y-start[3])**2)**0.5 >= r)\
        or (((x-start[0])**2 + (y-start[1])**2)**0.5 >= r) and (((x-start[2])**2 + (y-start[3])**2)**0.5 <= r):
            count += 1  # 출발점에서 행성의 중심과의 거리가 반지름보다 작고 도착점에서 행성의 중심과의 거리가 반지름보다 크거나
                        # 출발점에서 행성의 중심과의 거리가 반지름보다 크고 도착점에서 행성의 중심과의 거리가 반지름보다 작으면
                        # 행성계 진입 / 이탈한 것이므로, count 변수 + 1  
    print(count)        # count 변수 출력