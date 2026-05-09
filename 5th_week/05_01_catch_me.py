from collections import deque

c = 11
b = 2

# c = 11, 12,     14,   17,   21
# b = 2 , 1 ,     0, 2,
        # 2 ,     1, 3, 4
        # 4 ,     3, 5, 8
# 모든 경우의 수 나열 ==> BFS ==> Queue를 이용 + 시간과 위치를 같이 저장해야한다.
 
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0)) # 브라운 위치, 시간

    visited = [{} for _ in range(200001)] # (브라운 위치, 시간에 대한) 기록을 담아둘 곳

    # visited = [위치: {시간1: True, 시간2: True} , ...]
    # visited[3] = {0: True, 3: True} // 위치 3에 도달했을 때 시간들의 모음집을 dictionary에 저장
    # -> visited[위치][시간] = True

    while cony_loc < 200_000: 
        cony_loc += time

        if time in visited[cony_loc]: # -> 코니 로케이션이 visited[time]에 있는 dictionary 에 키 값으로 있는가?
            return time

        for i in range(0, len(queue)): # 큐에서 현재 위치를 뽑아와야한다. 그리고 업데이트 해야 한다.
            current_location, current_time = queue.popleft()

            new_time = current_time + 1
            # B -1 
            new_location = current_location - 1
            if 0 <= new_location <= 200_000:
                visited[new_location][new_time] = True
                queue.append((new_location, new_time))
                # print(visited[new_location])

            # B + 1
            new_location = current_location + 1 
            if 0 <= new_location <= 200_000:
                visited[new_location][new_time] = True
                queue.append((new_location, new_time))
            
            # 2 * b
            new_location = current_location * 2 
            if 0 <= new_location <= 200_000:    
                visited[new_location][new_time] = True
                queue.append((new_location, new_time))

        time += 1

# Q1. queue 에 어떻게 담아둘지?


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))