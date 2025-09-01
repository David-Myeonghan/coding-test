finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min_index = 0
    current_max_index = len(array) - 1
    current_guess_index = (current_min_index + current_max_index) // 2

    while current_min_index <= current_max_index:
        if array[current_guess_index] == target:
            return True
        elif array[current_guess_index] < target: # UP
            current_min_index = current_guess_index + 1
        elif array[current_guess_index] > target: # DOWN
            current_max_index = current_guess_index - 1
        current_guess_index = (current_min_index + current_max_index) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)