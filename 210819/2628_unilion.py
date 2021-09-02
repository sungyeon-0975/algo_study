import sys
input = sys.stdin.readline

col, row = map(int, input().split())
paper_list = []
result = 0
tc = int(input())
for _ in range(tc):
    paper_list.append(list(map(int, input().split())))





zero = [0, row]
one = [0, col]
for paper in paper_list:
    if paper[0] == 0:
        zero.append(paper[1])
    else:
        one.append(paper[1])

zero.sort()
result = []    
for i in range(1, len(zero)):
    result.append(zero[i] - zero[i - 1])

one.sort()
result2 = []    
for j in range(1, len(one)):
    result2.append(one[j] - one[j - 1])

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