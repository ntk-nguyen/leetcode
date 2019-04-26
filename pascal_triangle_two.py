"""
Pascal Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
"""


def pascal_triangle_two(num_rows):
    result = [1]
    try:
        for i in range(1, num_rows+1):
            result = [sum(x) for x in zip(result + [0], [0] + result)]
        return result
    except IndexError:
        return result


if __name__ == '__main__':
    number_of_rows = 1
    pascal_result = pascal_triangle_two(num_rows=number_of_rows)
    print(pascal_result)
