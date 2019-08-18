# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    length_list = []
    market_list = []

    for outside in coordinates:
        for inside in coordinates:
            if (distance(outside, inside) == 0):
                pass
            else:
                length_list.append(distance(outside, inside))
                market_pair = [outside, inside]
                market_list.append(market_pair)

    min_index = length_list.index(min(length_list))
    
    return market_list[min_index]



# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))