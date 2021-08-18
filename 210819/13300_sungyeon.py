import math

if __name__ == "__main__":
    n,k = map(int, input().split())
    students = [[0,0] for _ in range(7)]
    for _ in range(n):
        s, y = map(int, input().split()) #s=0은 여자, 1은 남자
        students[y][s] += 1
    
    print(sum(map(lambda x: math.ceil(x[0]/k) + math.ceil(x[1]/k), students)))