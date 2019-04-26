"""
Count the number of prime numbers less than a non-negative number, n.
Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


def count_primes(n):
    """
    Count the number of prime numbers less than a non-negative number, n
    :param n:
    :return:
    """
    number_array = list(range(2, n))
    counts = 0
    while len(number_array):
        divisor = min(number_array)
        if divisor > max(number_array)**0.5:
            break
        if min(number_array) == divisor:
            counts += 1
        number_array = [p for p in number_array if p % divisor]
    return counts + len(number_array)


if __name__ == '__main__':
    number = 999983
    result = count_primes(n=number)
    print(result)
