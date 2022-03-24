word = input()
pattern = input()
table = [0] * len(pattern)


j = 0
for i in range(1, len(pattern)):
    while j > 0 and pattern[i] != pattern[j]:
        j = table[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

j = 0

for i in range(len(word)):
    while j > 0 and word[i] != pattern[j]:
        j = table[j-1]

    if word[i] == pattern[j]:
        if j == len(pattern) - 1:
            print(1)
            break
        else:
            j += 1

else:
    print(0)
