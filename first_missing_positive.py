"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""


def first_missing_positive(nums):
    min_smallest = 1
    max_smallest = 1
    min_positive = 1
    max_positive = 1
    for i in nums:
        if i > 0:
            min_smallest = min(i, min_smallest)
            max_smallest = min(i-1, min_smallest)
            min_positive = min(i, min_positive)
            max_positive = min(i, max_positive)
            print('Min %s and Max %s' % (min_smallest, max_smallest))
    return min(min_smallest, max_smallest)


if __name__ == '__main__':
    input_nums = [1, 2, 0]
    first_missing_positive(input_nums)
