import sys
input = sys.stdin.readline

for _ in range(4):
    square = list(map(int, input().split()))
    first_square = square[:4]
    second_square = square[4:]

    x1, y1, x2, y2 = first_square[0], first_square[1], first_square[2], first_square[3]
    r1, c1, r2, c2 = second_square[0], second_square[1], second_square[2], second_square[3]
    
    # 상 하 좌 우

    if y2 < c1 or c2 < y1 or x2 < r1 or r2 < x1:        # 범위 밖
        result = 'd'
    
    elif (x2 == r1) and ((y2 == c1) or (y1 == c2)) or\
        (x1 == r2) and ((y1 == c2) or (y2 == c1)) or\
        (y1 == c2) and ((x1 == r2) or (x2 == r1)) or\
        (y2 == c1) and ((x2 == r1) or (x1 == r2)):      # 이미 범위밖을 걸렀기에 내부만 따지게 됨, 그러면서 점이 겹치는 곳
        result = 'c'
    
    elif (x2 == r1) and ((y2 > c1) or (y1 < c2)) or\
        (x1 == r2) and ((y2 > c1) or (y1 < c2)) or\
        (y1 == c2) and ((x2 > r1) or (x1 < r2)) or\
        (y2 == c1) and ((x2 > r1) or (x1 < r2)):        # 한 면을 고정한 채로 최대로 왔다갔다 한 거리
        result = 'b'

    else:                                              # 그 외
        result = 'a'
    
    print(result)

        # 하 상 좌 우 순으로 따짐

    # if ((second_square[0] <= first_square[2] <= second_square[2]) and (first_square[3] < second_square[1]))\
    #     or ((second_square[0] <= first_square[0] <= second_square[2]) and (first_square[1] < second_square[3]))\
    #     or ((second_square[1] <= first_square[3] <= second_square[3]) and (first_square[2] < second_square[0]))\
    #     or((second_square[1] <= first_square[1] <= second_square[3]) and (first_square[0] < second_square[2]))\
    #     or ((second_square[0] < first_square[0] and first_square[2] < second_square[2]) and (second_square[1] < first_square[1] and first_square[3] < second_square[3]))\
    #     or ((first_square[0] < second_square[0] and second_square[2] < first_square[2]) and (first_square[1] < second_square[1] and second_square[3] < first_square[3]))\
    #     or ((second_square[0] <= first_square[0] and first_square[2] <= second_square[2]) and (first_square[1] < second_square[1] and second_square[3] < first_square[3]))\
    #     or ((first_square[0] <= second_square[0] and second_square[2] <= first_square[2]) and (second_square[1] < first_square[1] and first_square[3] < second_square[3])):
    #     result = 'a'


    # elif (first_square[3] == second_square[1]) or (first_square[1] == second_square[3])\
    #     or (first_square[2] == second_square[0]) or (first_square[0] == second_square[2]):
    #     result = 'c'
        
    # elif ((second_square[0] <= first_square[2] <= second_square[2]) and (first_square[3] == second_square[1]))\
    #     or ((second_square[0] <= first_square[0] <= second_square[2]) and (first_square[1] == second_square[3]))\
    #     or ((second_square[1] <= first_square[3] <= second_square[3]) and (first_square[2] == second_square[0]))\
    #     or((second_square[1] <= first_square[1] <= second_square[3]) and (first_square[0] == second_square[2])):
    #     result = 'b'


    # else:
    #     result = 'd'

    # print(result)