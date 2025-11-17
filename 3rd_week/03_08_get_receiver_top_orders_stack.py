top_heights = [6, 9, 5, 7, 4]

# Stack 이용
# Stack 이라 치면 가장 오른쪽 탑부터 pop --> [6,9,5,7] -> 이 값들과 차례대로 비교
# 3,2,1,0 순으로 인덱스를 뽑아야한다.
# popped = heights.pop()

def get_receiver_top_orders(heights):
    result = [0] * len(heights)

    while heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, -1, -1):
            if height < heights[idx]:
                result[len(heights)] = idx + 1
                break

    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))