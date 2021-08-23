import sys
input = sys.stdin.readline

num = int(input())

# def solve():
#     lenlist = []
#     for second in range(num//2, num+1):
#         cont = [num, second]
#         next, i = 0, 0
#         while cont[i] - cont[i+1] >= 0:
#             next = cont[i] - cont[i+1]
#             cont.append(next)
#             i += 1
#         lenlist.append(len(cont))
#     second_idx = lenlist.index(max(lenlist))
#     real_second = num//2 + second_idx
#     real_cont = [num, real_second]
#     next, i = 0, 0
#     while real_cont[i] - real_cont[i+1] >= 0:
#         next = real_cont[i] - real_cont[i+1]
#         real_cont.append(next)
#         i += 1
#     return real_cont

# ans = solve()
# print(len(ans))
# print(*ans)


max_len = 0
max_list = []
for i in range(num//2, num+1):
    res = [num, i]
    j = 0
    while res[j] - res[j+1] >= 0:
        next = res[j] - res[j+1]
        res.append(next)
        if max_len < len(res):
            max_len = len(res)
            max_list = res[:]
        j += 1

print(max_len)
print(*max_list)