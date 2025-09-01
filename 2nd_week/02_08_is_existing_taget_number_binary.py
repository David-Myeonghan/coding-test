finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min_index = 0
    current_max_index = len(array) - 1
    current_guess_index = (current_min_index + current_max_index) // 2
    find_count = 0

    while current_min_index <= current_max_index:
        find_count += 1
        if array[current_guess_index] == target:
            print(find_count)
            return True
        elif array[current_guess_index] < target: # UP
            current_min_index = current_guess_index + 1
        elif array[current_guess_index] > target: # DOWN
            current_max_index = current_guess_index - 1
        current_guess_index = (current_min_index + current_max_index) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

# Array length: N
# 1st: 1 ... N
# 2nd: 1 ... N/2
# 3rd: 1 ... N/4
# kth: 1 ... N/2^k
#
# k번 탐색 -> N/2^k 개가 남는다
#
# N/2^k -> 1이 되려면, N = 2^k
# log_2(N) = K
#
# k 번 탐색시 원하는 1개 원소를 찾을 수 있다.
# O(log_2(N))
# ==> O(log(N))
#
# log(N) --> 연산량이 반씩 줄어들면 대강 로그N 이다!