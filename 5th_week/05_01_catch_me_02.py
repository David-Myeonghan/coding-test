from collections import deque

c = 11
b = 2

# 코니의 위치는 규칙적 -> 배열
# 브라운의 위치는 불규칙적 -> 모든 방문한 곳 저장 -> dict에 시간 저장 / dict를 배열에 저장  
# 브라운의 위치를 시간과 함께 저장해야한다.
# 모든 방문한 곳 -> BFS/DFS -> BFS = Queue / DFS = Stack

def catch_me(cony_loc, brown_loc):
    time = 0

    queue = deque()
    queue.append((brown_loc, time)) # queue에 처음값

    visited = [{} for _ in range(0, 200_000)]   # ❌ ① 크기 200_000 → 인덱스 0~199_999만 유효. 200_000 접근 시 IndexError. range(200_001) 이어야 함.
    visited[brown_loc] = {0: True} # []{}에 처음값

    while cony_loc <= 200_000:
        if cony_loc >= 200_000:
            return -1                            # ✅ ② OK (못 잡은 케이스 -1 반환)

        if time in visited[cony_loc]:            # ❌ ③ 순서 버그: cony_loc 갱신 *전*에 검사.
            return time                          #     예) iter2 (time=1)에 cony는 원본+1이어야 하는데
                                                 #         원본 위치로 검사 중. → `cony_loc += time`을 이 검사 *위*로 옮겨야 함.
        cony_loc += time

        for _ in range(0, len(queue)): # 큐에서 꺼내서, 그 다음값을 다시 큐에 넣고, visited에 기록해둬야함.
            current_location, current_time = queue.popleft()   # ✅ ④ OK (popleft가 for 안)

            new_time = current_time + 1

            new_location = current_location - 1
            if 0 <= new_location <= 200_000:                   # ❌ ⑧ 범위 한계 비일관: <=200_000 검사 vs visited 크기 200_000 (①과 함께 IndexError).
                queue.append((new_location, new_time))         # ✅ ⑤ OK (튜플로 묶음)
                visited[new_location][new_time] = True
                # ❌ ⑦ 중복 체크 누락: 조건에 `and new_time not in visited[new_location]` 추가해야
                #      같은 (위치, 시간)이 큐에 반복 삽입되어 폭발하는 걸 막을 수 있음.

            new_location = current_location + 1
            if 0 <= new_location <= 200_000:
                queue.append((new_location, new_time))
                visited[new_location][new_time] = True

            new_location = current_location + 2               # ❌ ⑥ 알고리즘 오류: '+2'가 아니라 '*2' (브라운은 b*2로 점프).
            if 0 <= new_location <= 200_000:
                queue.append((new_location, new_time))
                visited[new_location][new_time] = True

        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))


# =====================================================================
# 채점 결과
# =====================================================================
#
# ✅ 잘된 점
#   ② 못 잡는 경우 `return -1` 처리 OK.
#   ④ popleft가 for 루프 안에 있어 BFS 한 레벨이 정상 처리됨.
#   ⑤ queue.append((loc, time)) — 튜플로 묶어 인자 1개로 전달 OK.
#
# ❌ 고쳐야 할 점
#   ① visited 크기 200_000 → 200_001 로. 인덱스 200_000 접근 시 IndexError.
#   ③ `cony_loc += time` 위치 — visited 검사 *앞*으로 옮겨야 함.
#       지금: 검사 → 갱신 (틀림). 첫 iter는 우연히 맞지만 iter2부터 어긋남.
#       올바름: 갱신 → 범위 가드 → 검사.
#   ⑥ `current_location + 2` → `current_location * 2` (브라운의 점프는 *2).
#   ⑦ 중복 체크 누락 — 각 if에 `and new_time not in visited[new_location]` 추가.
#       이게 없으면 큐가 매 레벨 ~3배로 폭발해서 timeout. **가장 본질적 버그**.
#   ⑧ 범위 한계 비일관 — `new_location <= 200_000` 검사하면서 visited 크기는
#       200_000인 모순. ①을 200_001로 고치면 같이 해결됨.
#
# 우선순위
#   ⑦(폭발 방지) → ⑥(알고리즘 의미) → ③(타이밍) → ①⑧(범위) → 그 외
# =====================================================================