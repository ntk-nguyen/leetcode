"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
"""


def excel_sheet_column_title(n):
    alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    if n <= len(alphabet):
        return alphabet[n-1]
    if n % len(alphabet):
        return excel_sheet_column_title(int(n / len(alphabet))) + excel_sheet_column_title(n % len(alphabet))
    else:
        return excel_sheet_column_title(int(n / len(alphabet)) - 1) + excel_sheet_column_title(n % len(alphabet))


if __name__ == '__main__':
    number = 701
    result = excel_sheet_column_title(n=number)
    print(result)
