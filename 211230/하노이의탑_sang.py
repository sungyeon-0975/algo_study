def solution(n):
    answer = []

    def hanoi(n, dep, arr, via):
        if n == 1:
            answer.append([dep, arr])
            return
        # 보조기둥으로 이동
        hanoi(n-1, dep, via, arr)

        # 가장 아래 원반 이동
        answer.append([dep, arr])

        # 시작점 경유 후 최종으로 이동
        hanoi(n-1, via, arr, dep)

    hanoi(n, 1, 3, 2)

    return answer
