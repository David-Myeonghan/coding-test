def find_not_repeating_first_character(string):
    # dict 사용
    occurrence = {}
    for char in string:
        if char in occurrence:
            occurrence[char] += 1
        else:
            occurrence[char] = 1
    for key, value in occurrence.items():
        print(key, value)
        if value == 1:
            return key
    return "_"

def find_not_repeating_first_character_2(string):
    # 한번 순회를 돌면서 값을 array에 저장 - 알파벳 순 = 인덱스 순, 빈도수 + 1
    # 결과 array 를 돌면서 값이 1인 첫번째 인덱스를 찾는다.
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    print(alphabet_occurrence_array)
    for index in range(len(alphabet_occurrence_array)):
        occurrence = alphabet_occurrence_array[index]
        if occurrence == 1:
            return chr(index + ord('a'))
    return '_'


result = find_not_repeating_first_character_2
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))