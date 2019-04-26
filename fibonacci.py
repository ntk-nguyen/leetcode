"""
In mathematics, the Fibonacci numbers, commonly denoted Fn form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,[1]
F(0) = 0, F(1) = 1 and F(n) = F(n-1) + F(n-2)
"""


def fibonacci(n):
    if n < 0:
        raise ValueError('invalid n')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    number_of_iterations = range(-2, 15)
    for i in number_of_iterations:
        print('%s has a value of %s' % (i, fibonacci(i)))
