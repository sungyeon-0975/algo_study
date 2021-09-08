'''
실행시간 : 120ms
'''
def backtrack(res, idx):
    global temp, max_val, min_val
    if idx == n:
        if res > max_val:
            max_val = res
        if res < min_val:
            min_val = res
    
    for i in range(4):
        if temp[i] > 0:
            temp[i] -= 1
            backtrack(operators[i](res, l[idx]), idx + 1)
            temp[i] += 1


if __name__ == "__main__":
    operators = [
        lambda x,y: x+y,
        lambda x,y: x-y,
        lambda x,y: x*y,
        lambda x,y: -((-x)//y) if x<0 else x//y,
        ]
    n = int(input())
    l = list(map(int, input().split()))
    temp = list(map(int, input().split()))
    max_val, min_val = -1e9 , 1e9 
    backtrack(l[0],1)

    print(max_val)
    print(min_val)


