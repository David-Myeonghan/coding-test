input = 20

# def isPrime_brute_force(number):
#     if (number <= 1):
#         return False;
#     for i in range(2, number):
#         if (number % i == 0):
#             return False
#     return True

# 1. using flag.
def find_prime_list_under_number(number):
    # n % 2, n % 3, ..., n % (n -1)
    # 한번이라도 값이 0이면 소수 아님.
    prime_list = []
    for num in range(number + 1):
        isPrime = True
        if num <= 1:
            continue
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
        if isPrime:
            prime_list.append(num)
    return prime_list


# 2. for-else statement
def find_prime_list_under_number_2(number):
    prime_list = []
    for num in range(number + 1):
        if num <= 1:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
             prime_list.append(num)
    return prime_list

def find_prime_list_under_number_3(number):
    prime_list = []
    for num in range(number + 1):
        if num <= 1:
            continue
        for i in prime_list:
            if num % i == 0:
                break
        else:
            prime_list.append(num)
    return prime_list

def find_prime_list_under_number_4(number):
    prime_list = []
    for num in range(number + 1):
        if num <= 1:
            continue
        for i in prime_list:
            if i * i <= num and num % i == 0:
                break
        else:
            prime_list.append(num)
    return prime_list



### Keep in mind
# 1. range(n ,n)
#   -> 돌지 않음!

# 2. continue vs. break
# continue: 다음 루프로
# break: 루프 자체를 종료

# 3. for-else
# break 가 실행되지 않았으면,
# else 문 실행

# 4. 당황하지 말고, 과정을 설명해보자. - Don't panic!


result = find_prime_list_under_number_4(input)
print(result)