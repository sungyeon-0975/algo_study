import sys
input = sys.stdin.readline

col, row = map(int, input().split())
paper_list = []
result = 0
tc = int(input())
for _ in range(tc):
    paper_list.append(list(map(int, input().split())))
# paper_list.sort(key=lambda x:(x[0], x[1])) 
paper_list.sort()





zero = []
one = []
for paper in paper_list:
    if paper[0] == 0:
        zero.append(paper[1])
    elif paper[0] == 1:
        one.append(paper[1])

result = []    
for i in range(1, len(zero) - 1):
    result.append(zero[i + 1] - zero[i])
result.append(zero[0])
result.append(row - zero[-1])

result2 = []    
for j in range(1, len(one) - 1):
    result2.append(one[j + 1] - one[j])
result2.append(one[0])
result2.append(col - one[-1])

print(max(result) * max(result2))






# z = []
# o = []
# for i in range(len(zero) - 1):
#     z.append(zero[i + 1] - zero[i])
# z.append(zero[0])
# z.append(row - zero[(len(zero) - 1)])

# max_row = max(z)

# for j in range(len(one) - 1):
#     o.append(one[j + 1] - one[j])
# o.append(one[0])
# o.append(col - one[(len(one) - 1)])

# max_col = max(o)

# result = max_row * max_col

# print(result)