from collections import deque

c = 11
b = 2


MIN_LOCATION = 0
MAX_LOCATION = 200_000


def catch_me(cony_loc, brown_loc):
    time = 0

    # brown location BFS = queue / 기록 = list + dictionary
    queue = deque()
    queue.append((brown_loc, 0)) # 처음 위치 기록 - (위치, 초)

    visited = [{} for _ in range(0, MAX_LOCATION + 1)] # visited[위치] = {시간(초): True} / visited[1] = {3: True}
    visited[brown_loc] = ({0: True})

    while cony_loc <= MAX_LOCATION:
        cony_loc += time

        if (cony_loc > MAX_LOCATION): 
            return -1
        if (time in visited[cony_loc]):
            return time
        
        for _ in range(0, len(queue)): # 큐에서 꺼내서 다음 위치 업데이트 + 기록
            current_location, current_time = queue.popleft()

            new_time = current_time + 1
        
            new_location = current_location - 1
            if (MIN_LOCATION <= new_location <= MAX_LOCATION and not new_time in visited[new_location]):
                queue.append((new_location, new_time))
                visited[new_location][new_time] = True

            new_location = current_location + 1
            if (MIN_LOCATION <= new_location <= MAX_LOCATION and not new_time in visited[new_location]):
                queue.append((new_location, new_time))
                visited[new_location][new_time] = True

            new_location = current_location * 2  
            if (MIN_LOCATION <= new_location <= MAX_LOCATION and not new_time in visited[new_location]):
                queue.append((new_location, new_time))
                visited[new_location][new_time] = True

        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))