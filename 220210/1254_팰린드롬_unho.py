import sys
sys.stdin = open('input.txt')


S = list(sys.stdin.readline().strip())      # 입력 받은 문자열

idx = 0                                     # 오른쪽을 확인할 기준 인덱스
while True:
    if S[idx:] == S[idx:][::-1]:            # 인덱스를 기준으로 오른쪽의 문자들만 앞뒤로 뒤집었을때 팰린드롬인지 확인
        break
    idx += 1                                # 팰린드롬이 아니면 인덱스 증가

print(len(S) + idx)                         # 인덱스를 기준으로 오른쪽이 팰린드롬이 완성이라면, 왼쪽의 인덱스의 개수만큼 뒤에 붙이면 최소 길이의 팰린드롬 완성