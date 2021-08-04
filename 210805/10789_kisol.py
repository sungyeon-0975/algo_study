result = []

for i in range(15):
    result.append([])

for i in range(5):
    letter = input()
    for idx in range(len(letter)):
        result[idx].append(letter[idx])
    
for lst in result:
    for char in lst:
        print(char, end='')