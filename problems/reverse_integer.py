"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""


def reverse_integer(x: int):
    print('Return integer')
    if abs(x) > (2 ** 31 - 1):
        return 0
    elif x >= 0:
        reverse_x = str(x)[::-1]
    else:
        reverse_x = '-' + str(x)[1:][::-1]
    return int(reverse_x)


if __name__ == '__main__':
    num = 9646324351
    result = reverse_integer(x=num)
    print(result)
