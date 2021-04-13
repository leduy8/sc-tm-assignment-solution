
"""
Đề bài: Viết chương trình vẽ hình chữ nhật bằng dấu sao ( “*” )
(Số hàng và số cột phải là số tự nhiên dương lớn hơn 0)
Problem: Write a program to print rectangle star pattern.
(The number of rows and columns must be a natural positive number greater than 0)

Sample input: row = 3, column = 4
Sample output: ****
****
****
"""


def main(rows, cols):
    if rows < 0 or cols < 0 or type(rows) is not int or type(cols) is not int:
        return

    for _ in range(rows):
        for _ in range(cols):
            print('*', end='')
        print()


main(3, 4)
