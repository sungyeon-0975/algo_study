

t = int(input())

for i in range(t):
    sample = input()
    msum = 0
    cnt = 0

    for index in range(len(sample)):
        if sample[index] == 'O':
            cnt+=1
            msum += cnt

        if sample[index] == 'X':                
            cnt = 0   
            
    print(msum)