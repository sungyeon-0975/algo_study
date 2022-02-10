word = list(input())
l = len(word)

for i in range(l):
    if word[i:] == word[i:][::-1]:
        break

print(len(word) + i)
