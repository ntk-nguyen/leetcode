"""
Given an array of positive integers, find the contiguous subarray that sums to a given number X.

For example, input = [1,2,3,5,2] and X=8, Result = [3,5]

"""


def execute(a: list, target: int):
    if len(a) == 0 or a is None:
        return None
    start = end = 0
    subarray_sum = a[0]
    while start < len(a):
        if start > end:
            end = start
            subarray_sum = a[start]
        if subarray_sum < target:
            if end == len(a) - 1:
                break
            end += 1
            subarray_sum += a[end]
        elif subarray_sum > target:
            subarray_sum -= a[start]
            start += 1
        else:
            return a[start:end+1]
    return None


def test():
    a = [1, 2, 3, 5, 2]
    target = 8
    print(execute(a, target))