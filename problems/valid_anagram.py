"""
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
You may assume the string contains only lowercase alphabets.
"""


def is_anagram(s, t):
    hashmap_s = dict.fromkeys(s)
    hashmap_t = dict.fromkeys(t)
    if len(hashmap_s) != len(hashmap_t):
        return False
    try:
        for i in hashmap_s.keys():
            if s.count(i) != t.count(i):
                return False
    except KeyError:
        return False
    return True


if __name__ == '__main__':
    st = 'anagram'
    tt = 'nagara'
    result = is_anagram(s=st, t=tt)
    print(result)
