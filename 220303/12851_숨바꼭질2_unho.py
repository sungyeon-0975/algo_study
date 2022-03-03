import sys
import heapq
sys.stdin = open('input.txt')

def solution(start):
    heap = [(0, start)]                     # 시작 시간, 시작 좌표
    cnt = 0                                 # 동생에게 최단시간에 도착하는 방법 개수 카운트

    while heap:
        node = heapq.heappop(heap)         
        if distance[node[1]] >= node[0]:    # 다음 위치로 이동하는게 최소시간인 경우
            distance[node[1]] = node[0]     # 최소 시간 갱신
            if node[1] == K:                # 동생이 있는곳이라면 이동 방법 개수 카운트
                cnt += 1

            if node[1] - 1 >= 0:                                # 한칸 뒤로 이동이 유효한 범위인 경우 추가
                heapq.heappush(heap, (node[0]+1, node[1]-1))
            if node[1] + 1 <= 100000:                           # 한칸 앞으로 이동이 유효한 범위인 경우 추가
                heapq.heappush(heap, (node[0]+1, node[1]+1))
            if node[1] * 2 <= 100000:                           # 두배 이동이 유효한 범위인 경우 추가
                heapq.heappush(heap, (node[0]+1, node[1]*2))

    return cnt                                      # 동생에게 이동하는 방법 개수 반환

N, K = map(int, sys.stdin.readline().split())       # 수빈이 위치, 동생 위치
distance = [1e10] * 100001                          # 이동 가능한 범위의 리스트, 해당 좌표로 이동하기 위한 최소시간

answer = solution(N)                                # 수빈이 위치에서 출발

print(distance[K])                                  # 출력
print(answer)