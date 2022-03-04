import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())                                           # 테스트 케이스 개수

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())     # 좌표와 반지름
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5                           # 두 점간의 거리
    
    if x1 == x2 and y1 == y2 and r1 == r2:                  # 두 점이 같은 곳에 있고, 반지름도 같을때
        print(-1)
    elif distance == r1 + r2 or distance == abs(r1-r2):     # 두 원이 외접 또는 내접일때
        print(1)
    elif abs(r1-r2) < distance < r1 + r2:                   # 두 원이 바깥에서, 안에서 영역이 서로 겹칠때
        print(2)
    else:                                                   # 두 원이 서로 만나지 않을때
        print(0)