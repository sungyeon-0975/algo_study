def solution(n, info): # info: 어피치 기록
    # 가장 큰 점수 차이로 우승할 수 있는 방법 구하기 (못찾는 경우 [-1] return)
    max_res = 0
    result = []
    sel = [0] * 11
    check = [0] * 11

    def shoot(arrows, res, info):
        nonlocal max_res, sel, result, check
        if not arrows:  # 화살 다 쏜 경우
            if res > max_res:
                max_res = res
                result = sel[:]
            elif res == max_res:  # 여러 가지일 경우, 가장 낮은 점수부터 맞힌 개수가 더 많은 경우 찾기
                for k in range(10, -1, -1):
                    if result[k] < sel[k]:
                        result = sel[:]
                        break
                    elif result[k] > sel[k]:
                        break
            return
        for i in range(11):
            if not check[i]:  # 아직 안쏜 점수의 경우
                if arrows > info[i]:
                    sel[i] = info[i] + 1
                else:
                    for j in range(10, i, -1):
                        if arrows > info[j]:
                            sel[j] = arrows
                            break
                    else:
                        sel[i] = arrows
                check[i] = 1
                temp = res
                if info[i] > 0:
                    if sel[i] > info[i]:
                        res += (10 - i) * 2
                else:
                    res += (10 - i)
                shoot(arrows - sel[i], res, info)
                check[i] = 0
                sel[i] = 0
                res = temp
    shoot(n, 0, info)
    lion = 0
    apeach = 0
    # 라이언 총점과 어피치 총점 구하기
    for i in range(len(result)):
        if result[i] > info[i]:
            lion += (10 - i)
        elif info[i] > 0:
            apeach += (10 - i)
    if lion <= apeach:  # 비기는 경우에도 -1 return
        return [-1]
    return result

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])) # [1,1,1,1,1,1,1,1,0,0,2]

# 만약, k(k는 1~10사이의 자연수)점을 어피치가 a발을 맞혔고 라이언이 b발을 맞혔을 경우 더 많은 화살을 k점에 맞힌 선수가 k 점을 가져갑니다.
# 단, a = b일 경우는 어피치가 k점을 가져갑니다.
# k점을 여러 발 맞혀도 k점 보다 많은 점수를 가져가는 게 아니고 k점만 가져가는 것을 유의하세요.
# 현재 상황은 어피치가 화살 n발을 다 쏜 후이고 라이언이 화살을 쏠 차례입니다.

# 라이언은 어피치를 가장 큰 점수 차이로 이기기 위해서 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 구하려고 합니다.
# 이때, 라이언이 가장 큰 점수 차이로 우승하기 위해 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 10점부터 0점까지 순서대로 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
# 라이언이 우승할 수 없는 경우(무조건 지거나 비기는 경우)는 [-1]을 return 해주세요.
# info의 i번째 원소는 과녁의 10 - i 점을 맞힌 화살 개수
# 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
# 가장 낮은 점수를 맞힌 개수가 같을 경우 계속해서 그다음으로 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.