

word_list = []
for i in range(5):
    word = input()
    word_list.append(word)

result = ''
for i in range(15):
    for j in range(15):
        try:
            result += word_list[j][i]
        except:
            continue

print(result)

