"""
Type: Traversing Array in Reverse

Given a sentence, reverse the words of the sentence.
For example,
"i live in a house" becomes "house a in live i"

"""


def execute(a: str):
    reverse_a = ''
    word_end = len(a)
    i = len(a) - 1
    while i >= 0:
        if a[i] == ' ':
            reverse_a += a[i+1:word_end] + ' '
            word_end = i
        i -= 1
    return reverse_a


def test():
    a = "i live in a house"
    print(execute(a))
