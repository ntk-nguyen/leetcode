"""
Find longest common prefix
Example:
Input: ["flower","flow","flight"]
Output: "fl"
"""


def longest_common_prefix(strs):
    """
    Find longest common prefix
    :param strs:
    :return:
    """
    longest_prefix = ''
    if len(strs) == 0:
        return longest_prefix
    length_string = [len(s) for s in strs]
    shortest_string = strs[[i for i in range(len(strs)) if length_string[i] == min(length_string)][0]]
    for i in range(1, len(shortest_string)+1):
        sub_string = shortest_string[0:i]
        n = 0
        for j in range(0, len(strs)):
            if strs[j][0:i] == sub_string:
                n += 1
        if n == len(strs):
            longest_prefix = sub_string
        else:
            break

    return longest_prefix


if __name__ == '__main__':
    example_strings = ["a"]
    result = longest_common_prefix(example_strings)
    print(result)