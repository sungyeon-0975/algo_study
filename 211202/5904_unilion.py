import sys
input = sys.stdin.readline

'''
0 = 3
1 = 3 + (1 + 2 + 1) + 3 = 10
2 = 10 + (2 + 2 + 1) + 10 = 25
3 = 25 + 25 + (3 + 2 + 1) = 56

3
3 * 2 + 4
10 * 2 + 5
25 * 2 + 46

3 4 3 5 3 4 3 6 3 4 3 5 3 4 3 7
4 5 4 6 4 5 4 7

1 4 8 11 16 19 23 26 32 35 39 42 47 50 54 57 64
1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 5 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 6
2 3 2 4 2 3 2 5 2 3 2 4 2 3 2 6 
CNT = 0
RESULT = 1
K = 0
while RESULT < K:

IF CNT % 2:
K + 1
ELSE:
K = 2
'''

# N = int(input())
# r = 3
# k = 0
# temp = k + r
# cnt = 0
# temp_list = [1, 2]
# while temp < N:
#     temp_num = temp_list[cnt - 1]
#     k = temp * 2
#     r += 1
#     cnt += 1
#     temp = k + r
#     temp_list.append([*temp_list[cnt - 1]])
#     temp_list[cnt] += ['m']
#     for _ in range(cnt + 2):
#         temp_list[cnt] += ['o']
#     temp_list[cnt] += temp_list[cnt - 1]
# print(temp_list[cnt][N - 1])
















# S(N)은 S(N-1) + M + O x (n + 2) + S(N-1)

# N_list = ['m','o','o']
# def solve(N):
#     if len(N_list) >= n:
#         return
#     temp = N_list[:]
#     N_list.append('m')
#     for _ in range(N + 2):
#         N_list.append('o')
#     for i in temp:
#         N_list.append(i)
#     solve(N + 1)
#
#
#
# n = int(input())
# if n <= 3:
#     if n == 1:
#         print('m')
#     else:
#         print('o')
# else:
#     solve(1)
#     print(N_list[n-1])


## 구글링 이해..29200KB	68ms
n = int(input())
s = 3
k = 4
while n > s:
    s = s * 2 + k
    k += 1

k -= 1
while True:
    t = (s - k) / 2
    if (n <= t):    # 왼쪽 부분
        k -= 1
        s = t

    elif (n > t + k):   # 오른쪽 부분
        n -= (t + k)
        k -= 1
        s = t

    else:       # 가운데 부분
        n -= t
        break

if n == 1:
    print('m')
else:
    print('o')