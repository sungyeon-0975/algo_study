import sys



# 크로아티아 문자
CROATIA = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

in_str = sys.stdin.readline().strip()

# 입력받은 문자열 안에 크로아티아 문자가 포함되어 있으면 'a'로 변환
for cro in CROATIA:
    if cro in in_str:
        in_str = in_str.replace(str(cro), 'a')

print(len(in_str))