import sys

width, height = map(int, sys.stdin.readline().split())
num = int(sys.stdin.readline())

wid = [0, width]                                        # 시작점과 끝점 초기 설정
hei = [0, height]

for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())

    if a:                                               # 세로로 자르면 가로 길이 리스트에 추가
        wid.append(b)
    else:                                               # 가로로 자르면 세로 길이 리스트에 추가
        hei.append(b)

wid.sort()                                              # 자른 구간에 따라 만들어진 길이 계산을 위해 정렬
hei.sort()

wid = [(wid[i+1] - wid[i]) for i in range(len(wid)-1)]  # 뒤에 인덱스에서 앞에 인덱스를 빼면 잘리고 남은 길이가 구해짐
hei = [(hei[i+1] - hei[i]) for i in range(len(hei)-1)]

max_area = 0                                            # 길이들끼리 곱해서 면적 구함
for w in wid:
    for h in hei:
        if max_area < (w * h):
            max_area = (w * h)

print(max_area)