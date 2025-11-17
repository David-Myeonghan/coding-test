top_heights = [6, 9, 5, 7, 4]

# 반복문 이용
# 가장 오른쪽 탑부터 왼쪽으로 쏘면서 반복.
# 1 2 3 4 5 || 5번째 탑부터 --> 탑5가 탑4보다 같거나 큰지 --> 탑5가 탑3보다 같거나 큰지 --> ... 탑5가 ... 탑1보다 같거나 큰지
# v v v v
# 1 2 3 4 || 4번째 탑부터
# v v v
# 1 2 3  || 3번째 탑부터
# v v
# 1 2  || 2번째 탑부터
# v
# --> 인덱스 4,3,2,1 순으로 뽑아야 한다. (맨 오른쪽 탑부터 비교)

# 5번째 탑부터 --> 탑5가 탑4보다 같거나 큰지 --> 탑5가 탑3보다 같거나 큰지 --> ... 탑5가 ... 탑1보다 같거나 큰지
# --> 인덱스 3,2,1 0 순으로 뽑아야 한다.

# 아래와 같은 반복문을 이용해야 한다.
# for i in range(4, 0, -1):
#     for j in range(i - 1, -1, -1):
#         print(i, j)

def get_receiver_top_orders(heights):
    result = [0] * len(heights)

    for i in range(len(heights) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if heights[i] < heights[j]:
                result[i] = j + 1
                break

    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))