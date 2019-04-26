"""
Difficulty: Easy
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twosum_bf(nums, target):
    """
    Brute Force
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]


def twosum_two_pass_hash_table(nums, target):
    """
    Two-pass Hash Table
    To improve our run time complexity, we need a more efficient way to check if the complement exists in the array.
    If the complement exists, we need to look up its index.
    What is the best way to maintain a mapping of each element in the array to its index? A hash table.

    We reduce the look up time from O(n)O(n) to O(1)O(1) by trading space for speed.
    A hash table is built exactly for this purpose, it supports fast look up in near constant time.
    I say "near" because if a collision occurred, a look up could degenerate to O(n)O(n) time.
    But look up in hash table should be amortized O(1)O(1) time as long as the hash function was chosen carefully.

    A simple implementation uses two iterations.
    In the first iteration, we add each element's value and its index to the table.
    Then, in the second iteration we check if each element's complement
        (target - nums[i]target−nums[i]) exists in the table.
    Beware that the complement must not be nums[i]nums[i] itself!

    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    nums_map = {nums[i]: i for i in range(0, len(nums))}
    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in nums_map.keys() and nums_map[complement] != i:
            return [i, nums_map[complement]]


def twosum_one_pass_hash_table(nums, target):
    """
    One pass hash table
    :param nums:
    :param target:
    :return:
    """
    nums_map = dict()
    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in nums_map.keys():
            return [i, nums_map[complement]]
        nums_map[nums[i]] = i


if __name__ == '__main__':
    number_list = [2, 7, 11, 15]
    sum_target = 26
    index = twosum_bf(number_list, sum_target)
    print('%s + %s = %s' % (number_list[index[0]], number_list[index[1]], sum_target))
    index = twosum_two_pass_hash_table(number_list, sum_target)
    print('%s + %s = %s' % (number_list[index[0]], number_list[index[1]], sum_target))
    index = twosum_one_pass_hash_table(number_list, sum_target)
    print('%s + %s = %s' % (number_list[index[0]], number_list[index[1]], sum_target))

