"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is
returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""


def mySqrt(x: int):
    left = 1
    right = x
    if x < 2:
        return x
    while left < right:
        middle = left + int((right - left) / 2)
        if middle**2 > x:
            right = middle
        elif middle**2 == x:
            return middle
        else:
            left = middle + 1
    return left - 1


if __name__ == '__main__':
    result = mySqrt(x=2)
    print(result)
