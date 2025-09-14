input = "abcba"


def is_palindrome_recursive(string):
    if string[0] != string[-1]:
        return False
    elif len(string) == 1:
        return True

    return is_palindrome_recursive(string[1:-1])

print(is_palindrome_recursive(input))