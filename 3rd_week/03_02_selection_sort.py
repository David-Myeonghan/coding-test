input = [4, 6, 2, 9, 1]

# i = 0, j = 5, (0...4)
# i = 1, j = 4, (1...4)
# i = 2, j = 3, (2...4)
# i = 3, j = 2, (3...4)

# Main point:
# arr_length = len(input)
# for i in range(arr_length- 1):        # i = array 시작하는 index
#   for j in range(arr_length - i):     # j = 탐색 횟수(array 탐색 범위). j 범위는 점점 작아져야, array 길이를 넘지 않는다.
#       print(i, j)                    # 끝나는 지점 i + j 는 고정되어있는 형태

# O(n^2)
def selection_sort(array):
    array_length = len(array)

    for i in range(array_length - 1):       # O(n)
        min_index = i
        for j in range(array_length - i):   # O(n)
            if array[min_index] > array[i + j]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))