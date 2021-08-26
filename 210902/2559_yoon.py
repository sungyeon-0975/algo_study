import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

'''
38188 KB / 136 ms
처음에 중첩 for문 써서 풀었더니 시간초과 남
'''

N, K = map(int, input().split())
temperature = list(map(int, input().split()))

temp = sum(temperature[:K])
max_temp = temp

for i in range(K, N):
    temp += temperature[i]
    temp -= temperature[i-K]
    if temp > max_temp:
        max_temp = temp

print(max_temp)