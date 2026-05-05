def is_num_pal(number) -> bool:
    """
    Checks if a number is a palindrome.
    :param number: a number or string of a number.
    :return: bool
    """
    num = str(number)
    return num == num[::-1]


def test_palindrome():
    number = 12255221
    assert is_num_pal(number) is True


def test_not_palindrome():
    number = 12255271
    assert is_num_pal(number) is False


def test_no_number_palindrome():
    number = ""
    assert is_num_pal(number) is True


def test_one_number_palindrome():
    number = 1
    assert is_num_pal(number) is True
