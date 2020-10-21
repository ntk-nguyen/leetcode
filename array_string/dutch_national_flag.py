"""
Given an array of integers A and a pivot, rearrange A in the following order:

[Elements less than pivot, elements equal to pivot, elements greater than pivot]

For example, if A = [5,2,4,4,6,4,4,3] and pivot = 4 -> result = [3,2,4,4,4,4,6,5]

Note: the order within each section doesn't matter.
"""


def execute(a: list, pivot: int):
    low_boundary = 0
    high_boundary = len(a) - 1
    i = 0
    while i <= high_boundary:
        if a[i] < pivot:
            temp = a[low_boundary]
            a[low_boundary] = a[i]
            a[i] = temp
            i += 1
            low_boundary += 1
        elif a[i] > pivot:
            temp = a[high_boundary]
            a[high_boundary] = a[i]
            a[i] = temp
            high_boundary -= 1
        else:
            i += 1
    return a


def test():
    a = [5, 2, 4, 4, 6, 4, 4, 7]
    print(execute(a, 3))