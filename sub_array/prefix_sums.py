"""
Given an array of integers, find the contiguous subarray that sums to 0.
The array can contain both negative and positive integers.

For example: Input = [2,4,-2,1,-3,5,-3], Result = [4,-2,1,-3]
"""


def find_contiguous_subarray_sum_zero(a: list):
    hash_table = dict()
    prefix_sum = 0
    for i in range(0, len(a)):
        prefix_sum += a[i]
        if prefix_sum == 0:
            return a[:i+1]
        if prefix_sum in hash_table:
            return a[hash_table[prefix_sum] + 1: i + 1]
        hash_table[prefix_sum] = i
    return None


def find_contiguous_subarray_sum_x(a: list, target):
    hash_table = dict()
    prefix_sum = 0
    for i in range(0, len(a)):
        prefix_sum += a[i]
        print(prefix_sum)
        if prefix_sum == target:
            return a[:i+1]
        if prefix_sum - target in hash_table:
            return a[hash_table[prefix_sum - target] + 1: i + 1]
        hash_table[prefix_sum] = i
    return None


def test():
    a = [0, 4, -4, 0, -3, 5, -3]
    print(find_contiguous_subarray_sum_zero(a))
    a = [2, 4, -2, 1, -3, 5, -3]
    print(find_contiguous_subarray_sum_x(a, 5))
