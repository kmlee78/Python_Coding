"""위치 마다 특정 크기의 칸막이가 설치되어 있는 정보가
담긴 배열을 받으면 그곳에 담겨 있는 빗물의 최대 수를 
리턴하는 함수"""

def trapping_rain(buildings):
    rain = 0
    for x in range(len(buildings)):
        big_1 = 0
        big_2 = 0
        # 오른쪽에 있는 칸막이들 중 가장 큰 칸막이
        for i in range(x+1, len(buildings)):
            if buildings[i] >= big_1:
                big_1 = buildings[i]
        # 왼쪽에 있는 칸막이들 중 가장 큰 칸막이
        for j in range(1, x+1):
            if buildings[x-j] >= big_2:
                big_2 = buildings[x-j]
        # 두 칸막이들 중 작은 것을 고르고 그걸 기준으로 계산
        big = min(big_1, big_2)
        if big > buildings[x]:
            rain += (big - buildings[x])
    return rain

"""
def trapping_rain(buildings):
    rain = 0
    for i in range(1, len(buildings) - 1):
        big_1 = max(buildings[:i])
        big_2 = max(buildings[i:])

        big = min(big_1, big_2)

        rain += max(0, big - buildings[i])
    return rain
"""

print(trapping_rain([3, 0, 0, 2, 0, 4]))        # 10
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))      # 6