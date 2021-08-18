def solution(array, commands):
    answer = []
    for i,j,k in commands:
        sub=sorted(array[i-1:j])
        answer.append(sub[k-1])
    return answer