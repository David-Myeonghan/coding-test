# MergeSort(0, N) = Merge(MergeSort(0, N/2) + MergeSort(N/2, N))
# (원소 갯수가 한 개가 될 때까지) array를 계속 반으로 쪼개면서 sort 하는 방법도 있다. --> 재귀 함수

### 왜? (0 + len(array)) // 2
# --> 구간을 반으로 나눌 때 일반화된 형태로 쓰인다
# mid = (left + right) // 2
# left: 탐색 구간의 시작 인덱스
# right: 탐색 구간의 끝(또는 끝 + 1) 인덱스

array = [5, 3, 2, 1, 6, 8, 7, 4]
def merge_sort(array):
    if len(array) == 1:
        return array
    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(left_array, right_array)

# 시간 복잡도 - len(array1 + array2) 개 만큼 계산 O(n)
def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index += 1

    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index += 1

    return result

### merge_sort() 시간 복잡도
# 크기가 n -> n / 2 --> n / 2^2 --> n / 2^3  --> ... --> 1
# k 번 만큼 2로 나눠서 1이 되는 순간 --> 즉 N/2^k = 1
# k = log(2)N!

# merge() 호출 횟수 * merge() 시간 복잡도 = O(logN*N)

print(merge_sort(array))

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))