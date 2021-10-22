# def solution(word):
#     answer = 0
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     for k in range(4, -1, -1):
#         if k >= len(word):
#             answer = answer * 5 + 6
#         elif word[k] != 'A':
#             answer += answer * (len(word) - k - 1) + vowels.index(word[k]) + 1
#         elif word[k] == 'A':
#             answer += 1
#     return answer

def make_words(char, idx):
    if idx > 4:
        return
    for i in range(len(char)):
        temp = char[i]
        for j in range(5):
            if temp + vowels[j] not in words:
                words.append(temp + vowels[j])
    make_words(words, idx + 1)

def solution(word):
    return words.index(word) + 1

vowels = ['A', 'E', 'I', 'O', 'U']
words = vowels
make_words(vowels, 1)
words.sort()

print(solution('AAAAE'))
print(solution('AAAE'))
print(solution('I'))
print(solution('EIO'))