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
    # Sieve of Eratosthenes

    # We are only interested in numbers LESS than the input number
    # exit early for numbers LESS than 2; (two is prime)
    if n < 2:
        return 0
    number_array = [1] * n
    number_array[0] = 0
    number_array[1] = 0
    for i in range(2, int(n**0.5)+1):
        if number_array[i] != 0:
            number_array[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
    return sum(number_array)


if __name__ == '__main__':
    number = 999983
    result = count_primes(n=number)
    print(result)
