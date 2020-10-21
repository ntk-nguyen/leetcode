"""
Type: Traversing Array in Reverse

Given an array of numbers, replace each even number with two
of the same number. e.g, [1,2,5,6,8, , , ,] -> [1,2,2,5,6,6,8,8].

Assume that the array has the exact amount of space to accommodate the result.

Q. How do you want to return the result?
A. Modify the input array.

Q. What would an empty element contain?
A. -1

"""


def execute(a: list):
    if a is None or len(a) == 0:
        return a
    end = len(a)
    i = get_last_number(a)
    while i >= 0:
        if a[i] % 2 == 0:
            end -= 1
            a[end] = a[i]
        end -= 1
        a[end] = a[i]
        i -= 1
    return a


def get_last_number(a: list):
    i = len(a) - 1
    while i >= 0 and a[i] == -1:
        i -= 1
    return i


def test():
    a = [1, 2, 5, 6, 8, -1, -1, -1]
    print(execute(a))
    a = []
    print(execute(a))