"""
Given an integer n, return the number of trailing zeroes in n!
Example:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
"""


def logb_x(x, b):
    if x < b:
        return 0
    return 1 + logb_x(x/b, b)


def trailing_zeroes(n):
    """
    Finding trailing zeroes for factorial
    Since we have many more even numbers than numbers divisible by 5, we just need to find multiple of 5
    :param n:
    :return:
    """
    a = n / 5
    if a < 5:
        highest_power = 0
    else:
        highest_power = 1
        while True:
            a = a / 5
            highest_power += 1
            if a < 5:
                break
    r = int(n/5)
    for i in range(2, highest_power+1):
        r += int(n/(5**i))
    return r


if __name__ == '__main__':
    number = 30
    result = trailing_zeroes(n=number)
    print(result)
