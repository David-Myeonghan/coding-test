prices = [1, 2, 3, 2, 3]

# 0번째 인덱스 요소를, 1,2,3,4 번째 인덱스 요소와 비교
# 그렇다면, i = 0 부터 1,2,3 까지 나와야 한다. (마지막 요소는 마지막이라서 0)
# j 는 첫번째 주식 가격 다음인 인덱스 1 부터, 마지막 인덱스 4까지 나와야 한다.
# i = 0; j = 1,2,3,4
# i = 1; j = 2,3,4
# i = 2; j = 3,4
# i = 3; j = 4
# i = 4; X

# 아래 활용
# for i in range(0, 4, 1):
#     for j in range(i + 1, 5 ,1):
#         print (i, j)


def get_price_not_fall_periods(prices):
    result = [0] * len(prices)

    for i in range(0, len(prices) - 1, 1):
        not_fall_period = 0
        for j in range(i + 1, len(prices), 1):
            if prices[i] <= prices[j]:
                not_fall_period += 1
            else:
                not_fall_period += 1
                break
        result[i] = not_fall_period

    return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))