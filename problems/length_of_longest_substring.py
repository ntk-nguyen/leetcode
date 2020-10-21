"""
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring(s):
    """
    :param s: str
    :return: int
    """
    start = length = 0
    used_characters = {}
    for index, character in enumerate(s):
        print(index, character)
        if character in used_characters and start <= used_characters[character]:
            start = used_characters[character] + 1
        else:
            length = max(length, index - start + 1)
        used_characters[character] = index
    return length


if __name__ == '__main__':
    example_string = 'abcccbaacdbbbbdbac'
    substring_length = length_of_longest_substring(s=example_string)
