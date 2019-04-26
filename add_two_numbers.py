"""
Difficulty: Medium
You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode(object):
    """
    Definition for singly-linked list
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    """
    Definition of linked list
    """
    def __init__(self, x: list):
        self.node = [ListNode(i) for i in x]
        for i in range(0, len(x)-1):
            self.node[i].next = self.node[i+1]


def add_two_numbers(l1, l2):
    """
    Add two numbers
    :param l1: ListNode
    :param l2: ListNode
    :return:
    """
    print('')


if __name__ == '__main__':
    list1 = LinkList([2, 4, 3])

