input = "11101101"

# 한번의 행동:
# 연속된 숫자 블록을 한번 뒤집는 것.
# ie. 000 -> 111
# ie. 1 -> 0

# 분석: 전부  0으로 만들거나, 전부 1로 만들어야함.
# 모든 '0' 을 뒤집을 것이냐, 모든 '1' 을 뒤집을 것이냐를 판단해야함.
# 먼저, 이전 숫자와 다를 때, 즉 블록이 바뀌는 지점을 파악해야함 - 블록 전환 지점 카운트 (0에서 1이 되는 순간, 또는, 1에서 0이 되는 순간)
# --> '0' 인 그룹 갯수, '1' 인 그룹 갯수를 찾아서, 둘 중 작은 수를 반환. (모든 수를 0 또는 1로 뒤집을 때, 변경이 더 적은 수)

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_group_count = 0;
    one_group_count = 0;
    string_length = len(string)

    # 첫 글자에 대한 그룹 추가
    if string[0] == '0':
        zero_group_count += 1
    else:
        one_group_count += 1

    # index 1 부터 시작 - 현재 문자(string[i])를 이전 문자(string[i-1])와 비교 <-- 인덱스 에러 방지
    for index in range(1, string_length):
        current_char = string[index]
        prev_char = string[index - 1]

        if prev_char != current_char:
        # if string[index -1] != string[index]: # or,

        #     if current_char == '0': # or,
            if string[index] == '0':
                zero_group_count += 1
            else:
                one_group_count += 1


    print('zero: ', zero_group_count, 'one: ', one_group_count)
    return min(zero_group_count, one_group_count)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)