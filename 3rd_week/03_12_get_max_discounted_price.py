# Q.
# 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 1. shop_prices - 내림차순 정렬
# 2. user_coupons - 내림차순 정렬
# 3. 한쪽 원소가 떨어질 때까지 상품 가격 * (100 - discount) / 산00
# +) 쿠폰이 없으면 원가를 더하기
# 4. 더해서 리턴

def get_max_discounted_price(prices, coupons):
    prices.sort(reverse = True)
    coupons.sort(reverse = True)

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons): # 현재 가격과 쿠폰이 모두 배열 내의 원소일 때
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    # 쿠폰이 없을 때 원가 계산
    while price_index < len(prices): # 현재 price_index 가 prices 길이 범위 내라면,
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))