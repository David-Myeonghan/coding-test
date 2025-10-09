input = [4, 6, 2, 9, 1]

# Main point:
#   for i in range(len(array) - 1): --> 라운드
#       for j in range(len(array) - i - 1):  --> 라운드 당 비교 횟수


def bubble_sort(array):
    length = len(array)
    for i in range(length): # O(n)
        for j in range(length - i -1): # O(n)®
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
# O(n^2) Time complexity®

bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))