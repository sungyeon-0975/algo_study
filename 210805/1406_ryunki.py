import sys

N = list(sys.stdin.readline().strip())
my_list = []
repeat = int(sys.stdin.readline())

for i in range(repeat):
    command = sys.stdin.readline().strip()

    if command[0] == 'L' and N :
        my_list.append(N.pop())        
    
    elif command[0] == 'D' and my_list:
        N.append(my_list.pop())        
    
    elif command[0] == 'B' and N :
        N.pop()      
    
    elif command[0] == 'P':
        N.append(command[2])
    
print(''.join(N+my_list[::-1]))

# import sys

# N = list(sys.stdin.readline().rstrip())

# howmany = int(sys.stdin.readline())
# point = len(N)
# for i in range(howmany):    

#     command = list(sys.stdin.readline().split())

#     if command[0] == 'L' :
#         if point != 0:
#             point -= 1        
    
#     elif command[0] =='D':
#         if point != len(N):
#             point += 1
               
#     elif command[0] =='B':        
#         if point != 0:
#             del N[point-1]
#             point -= 1 

#     elif command[0] =='P':
#         N.insert(point,command[-1] ) 
#         point += 1       

# print(''.join(N))
# 시간초과