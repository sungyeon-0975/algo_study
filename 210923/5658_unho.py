import sys
sys.stdin = open('input_5658.txt')


T = int(input())
TRANS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input().strip()

    password = set()

    for i in range(N//4):
        for j in range(i, N, N//4):
            tmp = num[j:j+N//4]
            if j > (N - N//4):
                tmp += num[:i]

            password.add(tmp)
    
    tmp = sorted(password, reverse=True)[K-1]
    
    answer = 0
    for idx in range(N//4):
        answer += TRANS[tmp[-idx-1]] * (16**idx)

    
    print('#{} {}'.format(tc, answer))