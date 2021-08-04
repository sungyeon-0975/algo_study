from operator import xor

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x1,y1,x2,y2 = map(int, input().split())
        n = int(input())
        circle_list = [list(map(int, input().split())) for _ in range(n)]
        cnt = 0
        for a,b,r in circle_list:
            if xor((x1-a)**2 + (y1-b)**2 < r**2, (x2-a)**2 + (y2-b)**2 < r**2):
                cnt += 1
   
        print(cnt)
            

        

