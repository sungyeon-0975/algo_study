"""
29200KB 368ms
단순 수학
data[i][j] = a[i]&a[j] 각 행들은 두 수열의 교집합
a[i] = a[i] | data[i][j] 그렇다면 해당 수열은 행과 해당수열의 합집합
"""
import sys

sys.stdin = open('input_11811.txt')

for test in range(1, 1 + int(input())):
    N = int(input())
    temp = [0] * N

    for i in range(N):
        data = list(map(int, input().split()))
        for j in data:
            temp[i] |= j

    print(*temp)

# def main():
#     N = int(input())
#     temp = [0] * N
#
#     for i in range(N):
#         data = list(map(int, input().split()))
#         for j in range(N):
#             if i == j: continue
#             temp[i] |= data[j]
#     print(*temp)
#
# if __name__ == '__main__':
#     sys.exit(main())