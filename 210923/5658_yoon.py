import sys
sys.stdin = open('input_5658.txt')


def addingWords(line):
    global num
    for i in range(4):
        word = line[case*i:case*(i+1)]
        num.add(int(word, 16))


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    # 한 칸에 들어가는 숫자 수 (중복 나오지 않는)
    case = N//4
    num = set()
    line = input()

    for _ in range(case):
        line = line[-1:] + line[:-1]
        addingWords(line)

    num = sorted(list(num), reverse=True)
    print(f'#{t} {num[K-1]}')