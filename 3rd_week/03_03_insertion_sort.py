input = [4, 6, 2, 9, 1]

# 첫번째 요소 4는 정렬이 되어있기에, 2번째 요소 6부터 기준이 되는 4와 비교해서 정렬
# 인덱스 1번째 요소를 0번째 요소와 비교 -> 필요시 위치교환
# 인덱스 2번째 요소를 1번째 요소와 비교 -> 필요시 위치교환 -> 위치교환 했으면, 인덱스 1번째 요소를 0 번째 요소와 비교 -> 필요시 위치교환
# ...
# 인덱스 4번째 요소를 3번째 요소와 비교 -> 필요시 정렬 ...
# 이전 요소와 비교했을 때, 위치 교환이 필요 없다면, 그 이전 요소와도 비교할 필요 없다. (그 이전 요소들은 이미 정렬이 되어 있기 때문에)

# 일반적으로 O(n^2) 이지만,
# 오메가로 생각하면(= 최선의 경우) Ω(n) 일 수 있다. (이미 모두 정렬되어 있다면)
def insertion_sort(array):
    array_length = len(array)
    for i in range(1, array_length):    # O(n)
        for j in range(i):              # O(n)
            if array[i - j] < array[i - j -1]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break # 이미 앞에는 정렬되어 있어서, continue 가 필요 없음
    return array

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))