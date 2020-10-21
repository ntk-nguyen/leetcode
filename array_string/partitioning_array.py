"""
You are given an array of integers. Rearrange the array so that all zeroes are at the beginning of the array.

For example, [4,2,0,1,0,3,0] -> [0,0,0,4,1,2,3]

"""


def moving_zeroes_to_front_unordered(a: list):
    """
    Non-zero integers might not be in order after moving
    :param a:
    :return:
    """
    boundary = 0
    for i in range(0, len(a)):
        if a[i] == 0:
            a[i] = a[boundary]
            a[boundary] = 0
            boundary += 1
    return a


def moving_zeros_to_back_ordered(a: list):
    boundary = 0
    for i in range(0, len(a)):
        if a[i] != 0:
            temp = a[boundary]
            a[boundary] = a[i]
            a[i] = temp
            boundary += 1
    return a


def moving_zeros_to_front_ordered(a: list):
    """
    Non-zero integers will be in order after moving
    :param a:
    :return:
    """
    boundary = len(a) - 1
    for i in range(len(a) - 1, -1, -1):
        if a[i] != 0:
            temp = a[boundary]
            a[boundary] = a[i]
            a[i] = temp
            boundary -= 1
    return a


def test():
    a = [4, 2, 0, 1, 0, 3, 0, 5]
    b = moving_zeroes_to_front_unordered(a)
    print(b)
    a = [4, 2, 0, 1, 0, 3, 0, 5]
    b = moving_zeros_to_front_ordered(a)
    print(b)
    a = [4, 2, 0, 1, 0, 3, 0, 5]
    c = moving_zeros_to_back_ordered(a)
    print(c)
