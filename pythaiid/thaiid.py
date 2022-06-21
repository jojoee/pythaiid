from random import randint


def get_last_digit(checksum: int) -> int:
    """
    Get last digit (13th number) of Thai Nationality ID

    :param checksum:
    :return: single digit in range [0-9] e.g. 1, 4
    """
    return (11 - (checksum % 11)) % 10


def is_valid_checksum(s: str) -> bool:
    """
    Validate checksum value of Thai Nationality ID

    :param s:
    :return:
    """
    checksum = 0
    for i in range(0, 12):
        checksum += (13 - i) * int(s[i])

    return int(s[12]) == get_last_digit(checksum)


def verify(s: str = '') -> bool:
    """
    Verify Thai Nationality ID string

    :param s: string number e.g. "1234567891020", "3648905117022"
    :return:
    """
    # no null
    if not s:
        return False

    # string only
    if not isinstance(s, str):
        return False

    # must be number only
    if not s.isdigit():
        return False

    # length must match
    if len(s) != 13:
        return False

    # checksum
    if not is_valid_checksum(s):
        return False

    return True


def random() -> str:
    """
    Get random Thai Nationality ID

    :return: random generated Thai Nationality ID
    """
    checksum = 0
    s = ''

    for i in range(0, 12):
        r = randint(0, 9)
        checksum += (13 - i) * r
        s += str(r)

    return s + str(get_last_digit(checksum))
