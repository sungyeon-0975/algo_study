import sys

N = int(input())
my_list=[]

for i in range(N):
    my_list.append(list(map(int, sys.stdin.readline().split()))) # 시간초과

my_list.sort(key=lambda x:(x[0],x[1]))
for i in my_list:
    print(i[0],i[1])
# for index in range(N):
#     x,y = map(int,input().split())
#     my_list.append([x,y])


# for first in range(1,len(my_list)):
#     if my_list[first-1][0] > my_list[first][0]:
#         my_list[first-1],my_list[first]=my_list[first],my_list[first-1]

# for second in range(1,len(my_list)):
#     if my_list[second-1][0] == my_list[second][0]:
#         if my_list[second-1][1] > my_list[second][1]:            
#             my_list[second-1],my_list[second]=my_list[second],my_list[second-1]


# for i in range(len(my_list)):
#     for j in range(1,len(my_list[i])):
#         print(my_list[i][j-1],my_list[i][j])

