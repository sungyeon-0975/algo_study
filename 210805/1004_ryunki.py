import sys

T = int(sys.stdin.readline())

# 중심부터 원중심까지의 거리가 반지름보다 작으면  좌표가 원에 속해있다는 것을 의미 걸쳐진거 제외

for i in range(T):
    cnt = 0
    x,y,X,Y = map(int, sys.stdin.readline().split())
    t = int(sys.stdin.readline())
    for j in range(t):
        c,C,r = map(int, sys.stdin.readline().split())
        length_start = ((x-c)**2+(y-C)**2)**(1/2)
        length_arrive = ((X-c)**2+(Y-C)**2)**(1/2)
        if (r > length_start and r < length_arrive) or (r > length_arrive and r < length_start):
            cnt += 1
    print(cnt)



