numbers = [1, 1, 1, 1, 1]
target_number = 3

# 경우의 수를 생각해보자.
# [array_index, value]
# [0. +1]                                   || [0. -1]                                    # --> 0번째 인덱스 원소를 +1 하거나 -1 하는 경우 --> 2가지
# [1. 2]            | [1. 0]                || [1. 1]               | [1. -2]             # --> 위 결과에 1번째 인덱스 원소를 +1 하거나 -1 하는 경우 --> 4가지
# [2. 3] | [2. 1]   || [2. 1] | [2. -1]     || [2. 2] | [2. 0]      || [2. -1] | [2. -3]  # --> 위 결과에 2번째 인덱스 원소를 +1 하거나 -1 하는 경우 --> 8가지
# ...
# --> 수학적 공식이 아닌, 경우의 수를 일일히 생각해보는게 더 빠름 - 재귀 함수를 이용해서.

result = []
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    get_all_ways_by_doing_plur_or_minus(array, 0, 0)

    target_number_count = 0
    for number in result:
        if (number == target):
            target_number_count += 1

    return target_number_count

def get_all_ways_by_doing_plur_or_minus(array, current_index, current_sum):
    print('current_index:', current_index, 'current_sum: ',current_sum)
    if current_index == len(array):
        return result.append(current_sum)
    get_all_ways_by_doing_plur_or_minus(array, current_index + 1, current_sum + array[current_index])
    get_all_ways_by_doing_plur_or_minus(array, current_index + 1, current_sum - array[current_index])


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
print('result: ', result)
