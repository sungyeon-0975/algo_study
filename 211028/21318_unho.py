import sys
sys.stdin = open('input.txt')


N =int(sys.stdin.readline())                                # 곡의 개수
difficult = list(map(int, sys.stdin.readline().split()))    # 난이도를 배열로 받음 (1 ~ N)
Q = int(sys.stdin.readline())                               # 질문의 개수
accumualte_sum = [0] * N                                    # 누적합을 이용
                                                            # 0번 인덱스는 0번부터 0번까지 연주했을때 실수 
                                                            # 1번 인덱스는 0번부터 1번까지 연주했을때 실수
                                                            # 2번 인덱스는 0번부터 2번까지 연주했을때 실수 ...

for i in range(N-1):                                        # N-2 번 인덱스까지 반복
    accumualte_sum[i+1] += accumualte_sum[i]                # 다음번의 누적합은 현재까지의 누적합을 기본적으로 가져가야함
    if difficult[i] > difficult[i+1]:                       # 현재 곡의 난이도가 다음곡보다 어렵다면
        accumualte_sum[i+1] += 1                            # 다음곡의 실수 1회 추가

for _ in range(Q):                                          # 질문을 받음
    x, y = map(int, sys.stdin.readline().split())           
    print(accumualte_sum[y-1] - accumualte_sum[x-1])        # 0번부터 Y번까지의 실수 횟수 - 0번부터 X번까지의 실수 횟수