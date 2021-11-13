def solution(files):
    answer = []
    for file in files:
        head_fin, num_fin = 0, 0
        for idx in range(1, len(file)):
            if not file[idx-1].isdigit() and file[idx].isdigit():
                head_fin = idx
            elif file[idx-1].isdigit() and not file[idx].isdigit():
                num_fin = idx
                break
        head = file[:head_fin]
        number = file[head_fin:num_fin]
        tail = file[num_fin:]
        answer.append((head, number, tail))
    answer.sort(key=lambda x:(x[0].lower(), int(x[1])))
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    return answer

print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))