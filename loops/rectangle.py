
"""
Bài 4: Viết chương trình vẽ hình chữ nhật bằng dấu sao ( “*” )
(Số hàng và số cột phải là số dương lớn hơn 0)
Exercise 4: Write a program to print rectangle star pattern.
(The number of rows and columns must be a positive number greater than 0)

Sample input: row = 3, column = 4
Sample output: ****
****
****
"""


def main(rows, cols):
    for _ in range(rows):
        for _ in range(cols):
            print('*', end='')
        print()


main(3, 4)
