"""
Pascal Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


def pascal_triangle(num_rows):
    result = [[0] * i for i in range(1, num_rows+1)]
    try:
        result[0] = [1]
        for i in range(1, num_rows):
            result[i] = [sum(x) for x in zip(result[i-1] + [0], [0] + result[i-1])]
        return result
    except IndexError:
        return result


if __name__ == '__main__':
    number_of_rows = 0
    pascal_result = pascal_triangle(num_rows=number_of_rows)
    print(pascal_result)
