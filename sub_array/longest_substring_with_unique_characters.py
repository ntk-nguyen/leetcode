"""
(Level: Medium) Given a String, find the longest substring with unique characters.

For example: "whatwhywhere" --> "atwhy"

"""


def execute(a: str):
    if a is None or a == '':
        return None
    start = end = 0
    length = 1
    hash_table = dict({a[0]: 0})
    result = a[0]
    while end < len(a) - 1:
        end += 1
        if a[end] in hash_table and hash_table[a[end]] >= start:
            start = hash_table[a[end]] + 1
        hash_table[a[end]] = end
        if end - start + 1 > length:
            length = end - start + 1
            result = a[start: end + 1]
    return result


def test():
    a = 'whatwhywhere'
    print(execute(a))
    a = 'wwwwa'
    print(execute(a))
    a = 'wwwwwww'
    print(execute(a))
