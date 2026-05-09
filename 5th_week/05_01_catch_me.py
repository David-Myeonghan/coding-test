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
    visited[brown_loc][0] = True # 시작 상태 기록. 위에서도 append 했으니까 visited에도 넣어줘야함. (t=0 일 때, cony==brown 케이스 대응)

    # visited = [위치: {시간1: True, 시간2: True} , ...]
    # visited[3] = {0: True, 3: True} // 위치 3에 도달했을 때 시간들의 모음집을 dictionary에 저장
    # -> visited[위치][시간] = True

    while cony_loc < 200_000:
        cony_loc += time
        if cony_loc > 200_000: # cony_loc += time 으로 범위 초과 시 인덱스 보호
            return -1

        if time in visited[cony_loc]: # -> 코니 로케이션이 visited[time]에 있는 dictionary 에 키 값으로 있는가?
            return time

        for i in range(0, len(queue)): # 큐에서 현재 위치를 뽑아와야한다. 그리고 업데이트 해야 한다.
            current_location, current_time = queue.popleft()

            new_time = current_time + 1
            # B -1
            new_location = current_location - 1
            if 0 <= new_location <= 200_000 and new_time not in visited[new_location]: # 범위 안에 있고, 같은 (위치, 시간)이 있으면 또 기록하지 않도록.
                # visited에 있는 dict에서는 중복 저장이 안되지만(자동 dedup), queue에 다시 같은 (위치, 시간)이 들어가면 또 다시 계산되고 무한히 들어가면서 timeout.
                # 그걸 막기 위한 필수 조건
                # 알고리즘적 의미로도, BFS에서 같은 값은 한번만 방문하는게 맞음 (알고리즘 문제가 완전 이진 트리라는 전제하)
                visited[new_location][new_time] = True
                queue.append((new_location, new_time))

            # B + 1
            new_location = current_location + 1
            if 0 <= new_location <= 200_000 and new_time not in visited[new_location]:
                visited[new_location][new_time] = True
                queue.append((new_location, new_time))

            # 2 * b
            new_location = current_location * 2
            if 0 <= new_location <= 200_000 and new_time not in visited[new_location]:
                visited[new_location][new_time] = True
                queue.append((new_location, new_time))

        time += 1

    return -1 # cony_loc 이 정확히 200_000 도달 후 자연 종료된 경우

# Q1. queue 에 어떻게 담아둘지?


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))


# =====================================================================
# 변경점 정리 (왜 각 수정이 필요했는가)
# =====================================================================
#
# ① visited[brown_loc][0] = True  (시작 상태 등록)
#    - BFS에서 큐에 (brown_loc, 0)을 넣었으면 visited에도 같은 상태를
#      마킹해야 큐와 visited가 한 스텝 어긋나지 않는다.
#    - 없으면: catch_me(2, 2) 같은 케이스(cony==brown at t=0)에서
#      `0 in visited[2]`가 False라 정답 0을 못 잡고 한참 뒤에 잡음.
#
# ② cony_loc += time 직후 `if cony_loc > 200_000: return -1`
#    - visited 인덱스는 0~200_000까지만 유효.
#    - while 진입 조건 `cony_loc < 200_000`을 통과한 199_999에서
#      time을 더하면 200_000 초과 가능 → 다음 줄 visited[cony_loc]에서
#      IndexError로 크래시.
#    - 의미상: cony가 200_000 밖으로 나가면 더 잡을 수 없음 → -1.
#
# ③ 각 분기에 `and new_time not in visited[new_location]` 중복 체크
#    - 가장 본질적인 변경. 없으면 큐가 매 레벨 ~3배로 폭발해서
#      사실상 답이 안 나온다 (실측: 1→3→9→26→77→226→671→...).
#    - BFS 원칙: 이미 방문한 상태(여기선 (위치, 시간) 페어)는
#      재방문/재enqueue 금지.
#    - queue.append((new_location, new_time))도 여기서 같이 처리해야
#      하므로 visited 마킹 + enqueue를 한 블록 안에 묶음.
#
# ④ while 종료 후 `return -1`
#    - 명시적 return 없으면 함수가 None을 반환.
#    - cony_loc이 정확히 200_000을 찍고 다음 iter에서 조건이 거짓이 되어
#      자연 종료되는 경로를 위해 필요.
#    - ②와 같은 "못 잡음" 표시로 통일.
#
# 핵심 정리:
#   ①②④ : 정확성/안전성 (엣지 케이스 대응)
#   ③    : 알고리즘 정합성 (BFS의 상태 중복 방지) — 없으면 동작 불능
# =====================================================================