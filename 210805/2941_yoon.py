croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia: # 한 문자씩 찾아서 *로 바꿔줌
    word = word.replace(i, '*')

print(len(word))