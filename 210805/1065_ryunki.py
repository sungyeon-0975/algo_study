N = int(input())

num_list=[]
for i in range(1,N+1):
    n=i

    mlist = []
    while n>0:
        mlist.append(n%10)
        n //= 10
        
    diff = []
    if len(mlist)==1:
        diff.append(mlist[0])
    else:
        for j in range(1,len(mlist)):              
            diff.append(mlist[j-1]-mlist[j])   
    
    
    if len(set(diff))==1:
        num_list.append(i)
    

print(len(num_list))
