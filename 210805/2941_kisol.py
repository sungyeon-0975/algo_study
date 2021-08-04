croa = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

chars = input()
cnt = 0

while chars:
    cnt += 1
    if chars[0:3] == 'dz=':
        chars = chars[3:]
    elif chars[0:2] in croa:
        chars = chars[2:]
    else:
        chars = chars[1:]

print(cnt)