shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", '순대']

def is_available_to_order(menus, orders):
    menus.sort() ## 메뉴 길이가 N 일 때, --> O(NlogN)
    for order in orders: ## 오더의 길이가 M 이라면 O(M)
        if not is_existing_target_number_binary(order, menus): ## O(logN)
            return False
    ## 따라서, O(NlogN) + O(M) + O(logN) == O((N+M)*log(N))
    ## -> 효율적이지 않음!
    return True


def is_existing_target_number_binary(target, array):
    current_min_index = 0
    current_max_index = len(array) - 1
    current_guess_index = (current_min_index + current_max_index) // 2
    print(current_guess_index)

    while current_min_index <= current_max_index:
        if array[current_guess_index] == target:
            return True
        elif array[current_guess_index] < target: # UP
            current_min_index = current_guess_index + 1
        elif array[current_guess_index] > target: # DOWN
            current_max_index = current_guess_index - 1
        current_guess_index = (current_min_index + current_max_index) // 2

    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)


### Unexptected, but solved
# def is_available_to_order(menus, orders):
#     order_length = len(orders)
#     available = 0
#     for menu in menus:
#         for order in orders:
#             if menu == order:
#                 available += 1
#     if order_length == available:
#         return True
#     return False
