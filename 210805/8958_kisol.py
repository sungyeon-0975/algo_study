T = int(input())

for i in range(T):
    case = input()
    cnt_O = 0
    result = 0

    for char in case:
        if char == 'O':
            cnt_O += 1
            result += cnt_O
        else:
            cnt_O = 0
            
    print(result)