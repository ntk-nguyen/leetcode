"""
Given a string s, find the longest substring in s and r.
"""


def longest_substring(s, r):
    longest_substring_mat = [[0] * (1 + len(r)) for i in range(1 + len(s))]
    x_longest = 0
    length = 0
    for i in range(1, len(s)+1):
        for j in range(1, len(r)+1):
            if s[i-1] == r[j-1]:
                longest_substring_mat[i][j] = longest_substring_mat[i-1][j-1] + 1
                if longest_substring_mat[i][j] > length:
                    length = longest_substring_mat[i][j]
                    x_longest = i
            else:
                longest_substring_mat[i][j] = 0
    return s[x_longest - length: x_longest]


if __name__ == '__main__':
    example_string = 'aba'
    result = longest_substring(s='aba', r='sdfafba')
    print(result)