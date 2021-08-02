T = int(input())

for t in range(T):
    line = input()
    score = 0

    def count_cont(shortline): # 각 자리의 점수 계산하는 함수
        if 'X' not in shortline: # 아예 다 'O'이면 길이 그대로 반환
            return len(shortline)
        else: # 중간에 X 끼어 있으면 reverse시킨다음에 X등장하는 index가 점수
            reverse = shortline[::-1]
            return reverse.index('X')
    
    score = 0
    for i in range(len(line)):
        if line[i] == 'X':
            continue
        else:
            score += count_cont(line[:i+1])

    print(score)