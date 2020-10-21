"""
Given an array of integers, find the contiguous subarray (with at least 1 element) with the maximum sum.

The array can contain both negative and positive integers.

"""


def execute(a: list):
    local_max_sum = a[0]
    global_max_sum = a[0]
    for i in range(0, len(a)):
        local_max_sum = max(a[i], local_max_sum + a[i])
        global_max_sum = max(global_max_sum, local_max_sum)
    return global_max_sum


def test():
    a = [-2, -3, 4, -1, -2, 1, 5, -1]
    print(execute(a))
    a = [-2, 3, -1, 5]
    print(execute(a))
