def find_max_plus_or_multiply(array):
    # 곱하기, 더하기 중 더 큰 숫자가 나오는 연산 방법을 택한다.
    acc = 0
    for element in array:
        if element + acc > element * acc:
            acc = element + acc
        else:
            acc = element * acc

    return acc


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))